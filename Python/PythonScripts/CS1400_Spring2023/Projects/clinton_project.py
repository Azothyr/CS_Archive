"""
Project Name: Was Clinton Right?
Author: Zachary Peterson
Due Date: 2023-05-03
Course: CS1400-x01

This code calculates the total number of private sector jobs created between 1961 and 2012 by US Presidents
of different political parties.It also reads data from two input files: 'BLS_private.csv' which contains the monthly
private sector job numbers, and 'presidents.txt' which contains the names, political parties and terms of US Presidents.
"""
import csv


def read_jobs_data(file_path):
    """Reads a CSV file of jobs data and returns a list of dictionaries, each dictionary containing the year
     and monthly job numbers."""
    jobs_data = []
    with open(file_path) as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i < 6:
                continue
            year = int(row[0])
            jan = int(row[1])
            feb = int(row[2])
            mar = int(row[3])
            apr = int(row[4])
            may = int(row[5])
            jun = int(row[6])
            jul = int(row[7])
            aug = int(row[8])
            sep = int(row[9])
            oct_ = int(row[10])
            nov = int(row[11])
            dec = int(row[12])
            jobs_data.append({
                'Year': year, 'Months': [jan, feb, mar, apr, may, jun, jul, aug, sep, oct_, nov, dec]
            })
    return jobs_data


def get_presidential_jobs(jobs_data, presidents_data):
    """
    Takes in a list of jobs data and a list of presidential data, and calculates the private sector jobs created
    during each presidential term. Returns the total jobs created by Democratic and Republican presidents.
    """
    dem_jobs = 0
    rep_jobs = 0

    for president in presidents_data:
        start_year = president['start_year']
        start_month = president['start_month']
        end_year = president['end_year']
        end_month = president['end_month']
        party = president['party']
        run_term_job = get_term_jobs(jobs_data, start_year, start_month, end_year, end_month)
        term_jobs = run_term_job
        if party == 'Democratic':
            dem_jobs += term_jobs
        else:
            rep_jobs += term_jobs

        print(
            f"{president['president']} ({party}) | Term: {start_month}-{start_year} "
            f"to {end_month}-{end_year}\n Private Sector jobs during term: {term_jobs:,}")
        print(f"---Democratic total: {dem_jobs:,}---")
        print(f"---Republican total: {rep_jobs:,}---")

    return dem_jobs, rep_jobs


def read_presidents_data(file_path):
    """
    Reads a text file of presidential data and returns a list of dictionaries, each dictionary containing the
    president's name, party affiliation, and the start and end dates of their term.
    """
    presidents_data = []
    with open(file_path) as file:
        for line in file:
            president, party, start_date, end_date = line.strip().split(',')
            start_year, start_month = map(int, start_date.split('-'))
            end_year, end_month = map(int, end_date.split('-'))
            presidents_data.append({
                'president': president,
                'party': party,
                'start_year': start_year,
                'start_month': start_month,
                'end_year': end_year,
                'end_month': end_month,
            })
    return presidents_data


def get_cumulative_total(jobs_data):
    """
    Takes in a list of jobs data and calculates the total private sector jobs created between 1961 and 2012.
    """
    cumulative_total = sum([sum(row['Months']) for row in jobs_data if 1961 <= row['Year'] <= 2012])
    return cumulative_total


def get_term_jobs(jobs_data, start_year, start_month, end_year, end_month):
    """
    Takes in a list of jobs data and the start and end dates of a presidential term, and calculates the private sector
    jobs created during that term.
    """
    term_jobs = 0
    start_month -= 1
    for row in jobs_data:
        year = row['Year']
        if start_year <= year <= end_year:
            month_range = range(0, 12)
            if start_year == end_year:
                month_range = range(start_month, end_month)
            if year == start_year:
                month_range = range(0, 12)
                special_run_start = False
                if start_month != 0:
                    special_run_start = True
                    month_range = range(0, 12 - (start_month+1))
            if year == end_year:
                if end_month == 1:
                    continue
                month_range = range(0, end_month)
            for month in month_range:
                if special_run_start:
                    term_jobs += row['Months'][month + start_month]
                else:
                    term_jobs += row['Months'][month]
            special_run_start = False
        else:
            continue

    return term_jobs


def main():
    """
    Runs the program by calling the above cus_funcs and checking if Clinton's claim about job creation is accurate.
    """
    jobs_data = read_jobs_data('BLS_private.csv')
    presidents_data = read_presidents_data('presidents.txt')
    dem_jobs, rep_jobs = get_presidential_jobs(jobs_data, presidents_data)
    cumulative_total = get_cumulative_total(jobs_data)

    print(f"Total private sector jobs created between 1961 and 2012: {cumulative_total:,}")
    print(f"Total private sector jobs created by Democratic presidents: {dem_jobs:,}")
    print(f"Total private sector jobs created by Republican presidents: {rep_jobs:,}")

    if dem_jobs > 42000000 and rep_jobs > 24000000:
        print("Clinton's claim is accurate.")
    else:
        print("Clinton's claim is not accurate.")


if __name__ == '__main__':
    main()
