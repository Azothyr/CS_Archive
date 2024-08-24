"""
Project Name: Project 3: Rabbits, Rabbits, Rabbits
Author: Zachary Peterson
Due Date: 2023-02-09
Course: CS1400-x01

This code is for a simple calculator that determines when you will run out of cages a month-to-month output
of rabbit pairs (adult, baby and total) to a csv document until cages are full. Creation from user input
of starting month, initial adult pair, baby pair and available cages.
"""
import csv
import os


def do_research(cage_count, initial_adult_count, initial_baby_count):
    """
    Take input of the amount of cages, initial amount of adult (rabbits older than 1 month) and baby rabbits.
    Calculate when we will run out of cages based on rabbit exponential growth month to month. Output to rabbits.csv.
    """
    rabbits_total = initial_adult_count + initial_baby_count
    month = 1
    transition_amount = 0
    current_adult_count = initial_adult_count
    current_baby_count = initial_baby_count

    with open(os.path.expanduser('~') + "/Downloads/rabbits.csv", "w") as output_file:
        writer = csv.writer(output_file)
        output_file.write('# Table of rabbit pairs\n')
        writer.writerow(['Month', ' Adults', ' Babies', ' Total'])
        writer.writerow([f'{month}', f' {current_adult_count}', f' {current_baby_count}', f' {rabbits_total}'])
        while rabbits_total < cage_count:
            month += 1
            transition_amount = current_baby_count
            current_baby_count = current_adult_count
            current_adult_count += transition_amount
            rabbits_total = current_adult_count + current_baby_count
            writer.writerow([f'{month}', f' {current_adult_count}', f' {current_baby_count}', f' {rabbits_total}'])
        output_file.write(f'# Cages will run out in month {month}')


do_research(500, 1, 0)
