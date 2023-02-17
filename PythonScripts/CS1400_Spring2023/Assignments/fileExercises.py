# return number of lines and characters in a file------------------------------------
import sys

test_file = sys.argv[1]

line_count = 0
char_count = 0

with open(test_file, "r") as input_file:
    line = input_file.readline()
    while line != "":
        line_count += 1
        char_count += len(line)
        line = input_file.readline()

print("{} lines".format(line_count))
print("{} characters".format(char_count))

# get average from CSV---------------------------------------------------------------
import sys

test_file = sys.argv[1]

import csv
from collections import defaultdict

column_total = 0
average_column = []

columns = defaultdict(list)
with open(test_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter=',')
    row_values = next(reader)
    range = range(len(row_values))
    for nums in row_values:
        columns[row_values.index(nums)].append(nums)
    for row in reader:
        for column in range:
            columns[column].append(row[column])

for column in columns:
    num_list = columns[column]
    row_count = len(num_list)
    total = 0
    for num in num_list:
        total += float(num)
    average = (total / row_count)
    average_column.append(average)

for num in average_column:
    print(num, end=" ")

# Reverse lines from a file ---------------------------------------------------------
import sys

test_file = sys.argv[1]

with open(test_file, "r") as input_file:
  lines = input_file.readlines()
  lines.reverse()
  for line in lines:
    print(line)

# Get and compare csv data to get oldest person----------------------------------------
import sys, csv

test_file = sys.argv[1]
oldest_age = 0
oldest_name = ""

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter="\t")
    next(reader)
    for name, age, career in reader:
        if int(age) > oldest_age:
            oldest_age = int(age)
            oldest_name = name

print(f"The oldest person is {oldest_name}.")

# return string list of cities under the southern hemisphere
import sys, csv

test_file = sys.argv[1]
south_hemi = []

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter=",")
    next(reader)
    for city, country, latitude, longitude in reader:
        if int(latitude) < 0:
            name = city
            south_hemi.append(name)

string = ', '.join([str(item) for item in south_hemi])

print(f'The following cities are in the Southern Hemisphere: {string}.')