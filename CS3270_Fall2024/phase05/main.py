import logging as logfrom file_handler import FileHandlerfrom csv_handler import CSVHandlerfrom data_calculator import DataCalculator as DataCalcdef main():    """    Main function to run the program, opens a file dialog to select the data file to process.    """    # Initialize the FileHandler    file_handler = FileHandler()    try:        # Retrieve the file path using the FileHandler class        file_path = file_handler.retrieve_file()    except FileNotFoundError as e:        log.error(f"File not found: {e}")        return    except Exception as e:        log.error(f"Unexpected error: {e}")        return    # Initialize the CSVHandler    csv_handler = CSVHandler(file_path)    try:        # Use a generator to read data in chunks        data_generator = csv_handler.read_data_in_chunks()        for i, chunk in enumerate(data_generator):            log.info(f"Processing data chunk[{i}]")            # Iterate through each column in the DataFrame and perform analysis            for col in chunk:                analysis = DataCalc(chunk[col].tolist())                log.debug(                    f"Analysis for {col}"                    f"\n\tMean: {analysis.mean}"                    f"\n\tMedian: {analysis.median}"                    f"\n\tMode: {analysis.mode}"                    f"\n\tVariance: {analysis.variance}"                    f"\n\tStandard deviation: {analysis.standard_deviation}"                    f"\n\tMin: {analysis.min}"                    f"\n\tMax: {analysis.max}"                )    except Exception as e:        log.error(f"Error processing data: {e}")        returnif __name__ == "__main__":    # Set the log level to debug    log.basicConfig(        level=log.DEBUG,        format="| %(asctime)s | %(levelname)s | \n\t%(message)s\n",        datefmt="%Y-%m-%d (%H:%M:%S)",    )    main()