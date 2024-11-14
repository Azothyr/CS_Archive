from flask import Flask, request, redirect, url_for, render_template, flash, jsonify
from werkzeug.utils import secure_filename
import pandas as pd
from sqlalchemy import create_engine
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time
from concurrent_data_calculator import ConcurrentDataCalculator

app = Flask(__name__, template_folder=".", static_folder="static")
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv'}
app.secret_key = 'SUPER_secure&secret_KEY'

# Database setup
engine = create_engine('sqlite:///dataset.db')

if app.config['UPLOAD_FOLDER'] not in os.listdir():
    os.mkdir(app.config['UPLOAD_FOLDER'])
if "static" not in os.listdir():
    os.mkdir("static")

COLUMNS = []
NUMERIC_COLUMNS = []


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html', success=False, data=None)


@app.route('/analysis')
def analysis():
    return render_template('analysis.html', columns=COLUMNS, numeric_columns=NUMERIC_COLUMNS)


@app.route('/get_analysis', methods=['POST'])
def get_analysis():
    column = request.form['analysis-column']
    data_column = pd.read_sql('dataset', con=engine)[column].dropna().tolist()
    calc = ConcurrentDataCalculator(data_column)
    analysis_result = {
        'mean': f"{calc.mean:.4}" if isinstance(calc.mean, float) else calc.mean,
        'median': f"{calc.median:.4}" if isinstance(calc.median, float) else calc.median,
        'mode': str(calc.mode),  # Mode might be an array, so keep it as a string
        'variance': f"{calc.variance:.4}" if isinstance(calc.variance, float) else calc.variance,
        'standard_deviation': f"{calc.standard_deviation:.4}" if isinstance(calc.standard_deviation, float) else calc.standard_deviation,
        'min': f"{calc.min:.4}" if isinstance(calc.min, float) else calc.min,
        'max': f"{calc.max:.4}" if isinstance(calc.max, float) else calc.max
    }

    return jsonify(analysis_result)


@app.route('/get_data', methods=['GET'])
def get_data():
    page = request.args.get('page', 1, type=int)
    per_page = 30  # Number of rows per page

    # Query only the required rows based on the page
    data = pd.read_sql('dataset', con=engine)
    start = (page - 1) * per_page
    end = start + per_page
    loaded_data = data.iloc[start:end].to_dict(orient='records')

    # Return paginated data as JSON
    return {'data': loaded_data}


@app.route('/generate_visualization', methods=['POST'])
def generate_visualization():
    independent_variable = request.form.get('independent_variable')
    dependent_variable = request.form.get('dependent_variable')

    if not independent_variable or not dependent_variable:
        return jsonify({'error': 'Both independent and dependent variables must be selected for visualization'}), 400

    # Load data from database
    data = pd.read_sql('dataset', con=engine)

    # Check if the columns exist in the data
    if independent_variable not in data.columns or dependent_variable not in data.columns:
        return jsonify({'error': 'Selected columns are not found in the dataset'}), 400

    # Determine if the independent variable is numeric
    is_independent_numeric = pd.api.types.is_numeric_dtype(data[independent_variable])
    is_dependent_numeric = pd.api.types.is_numeric_dtype(data[dependent_variable])

    unique_values = data[independent_variable].nunique()
    if unique_values > 20:  # Limiting to top 20 for clarity
        top_categories = data[independent_variable].value_counts().nlargest(20).index
        data = data[data[independent_variable].isin(top_categories)]
        fontsize = 8
        figsize = (15, 10)
        description = "Top 20 "
    else:
        fontsize = 10
        figsize = (10, 6)
        description = ""

    plt.figure(figsize=figsize)

    # Conditional plotting
    if is_independent_numeric and is_dependent_numeric:
        # Scatter plot for numeric-independent and numeric-dependent variables
        plt.scatter(data[independent_variable], data[dependent_variable], color='skyblue')
        plt.xlabel(independent_variable)
        plt.ylabel(dependent_variable)
        plt.xticks(rotation=90, ha="right", fontsize=fontsize)
        plt.title(f'{dependent_variable} vs {description}{independent_variable}')
    elif is_dependent_numeric:
        # Box plot for categorical-independent and numeric-dependent variables
        data.boxplot(column=dependent_variable, by=independent_variable)
        plt.xticks(rotation=90, ha="right", fontsize=fontsize)
        plt.suptitle(f'{dependent_variable} by {description}{independent_variable}')
        plt.title("")
        plt.xlabel(independent_variable)
        plt.ylabel(dependent_variable)
    else:
        counts = data.groupby([independent_variable, dependent_variable]).size().unstack(fill_value=0)
        counts.plot(kind='bar', stacked=True, figsize=figsize)
        plt.xticks(rotation=45, ha="right", fontsize=fontsize)
        plt.title(f'{dependent_variable} by {independent_variable}')
        plt.xlabel(independent_variable)
        plt.ylabel("Count")

    timestamp = int(time.time())
    image_filename = f'visualization_{timestamp}.png'
    image_path = os.path.join('static', image_filename)
    plt.savefig(image_path)
    plt.close()

    # Return the image path to the frontend
    return jsonify({'image_url': url_for('static', filename=image_filename)})


@app.route('/upload', methods=['POST'])
def upload_file():
    global COLUMNS, NUMERIC_COLUMNS
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        file.save(file_path)

        try:
            data = pd.read_csv(file_path)

            # Identify numeric columns
            COLUMNS = data.columns.tolist()
            NUMERIC_COLUMNS = data.select_dtypes(include=['number']).columns.tolist()

            data.to_sql('dataset', con=engine, if_exists='replace', index=False)
            flash('File successfully uploaded and processed')

            # Preview the first 5 rows for display in the index page
            data_preview = data.head().to_dict(orient="records")
            os.remove(file_path)

            return render_template('index.html', success=True, data=data_preview, numeric_columns=NUMERIC_COLUMNS)

        except Exception as e:
            flash(f'An error occurred while processing the file: {e}')
            os.remove(file_path)
            return redirect(url_for('index'))
    else:
        flash('Allowed file type is CSV')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)