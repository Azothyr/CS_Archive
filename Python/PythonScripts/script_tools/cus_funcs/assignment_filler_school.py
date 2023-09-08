from pywinauto.application import Application
from pywinauto import Desktop
import time


def get_lines():
    date = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
    check_for = ('module', 'sri', 'exam', 'final', 'homework', 'discuss', 'quiz')
    write_lines = []
    with open('assignment_data.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            check_line = line.split()
            for word in check_line:
                if word.lower() in date or word.lower() in check_for:
                    write_lines.append(line)
                    break
    return write_lines


def refine_text(txt):
    to_remove = ('Homework', 'Module Exams', 'Quizzes', 'Projects', 'Programming', 'discussions')
    to_replace = ' by 11:59pm'
    check_for = ('Complete | ', 'Submit | ', ' (Remotely Proctored)')

    assignments = {}
    homeworks = []
    dates = []

    for value in txt:
        if value in to_remove:
            continue

        # Handle date replacements
        replaced_date = value.replace(to_replace, '')
        if replaced_date != value:
            dates.append(replaced_date)
            continue

        # Handle homework replacements
        if any(value.startswith(prefix) for prefix in ('Module', 'SRI', 'Final')):
            for v in check_for:
                value = value.replace(v, '')
            homeworks.append(value)

    # Pair up homeworks and dates based on order
    for hw, date in zip(homeworks, dates):
        assignments[hw] = date

    return assignments


def write_result_to_file(data):
    with open('result.txt', 'w') as f:
        for key, value in data.items():
            f.write(f'{key} {value}\n')


def type_and_enter(data, app_name):
    # Connect to the application
    app = Application().connect(title_re=app_name)

    # This assumes there's only one window of the app open
    dlg = app.window(title_re=app_name)

    for assignment, date in data.items():
        line = f"{assignment} {date}"
        dlg.type_keys(line, with_spaces=True)
        time.sleep(0.1)
        dlg.type_keys("{ENTER}")


def get_app_names():
    windows = Desktop(backend="win32").windows()
    apps = []
    for w in windows:
        line = w.window_text()
        if line:
            apps.append(line)
    return '\n'.join(sorted(set(apps)))


def main():
    # print(get_app_names())
    text = refine_text(get_lines())
    time.sleep(2)
    type_and_enter(text, '● 2023 Fall Semester - Asana')


if __name__ == "__main__":
    main()
