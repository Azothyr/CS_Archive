""" lines:
I've got a lovely bunch of coconuts
There they are, all standing in a row
"""
with open('coconuts.txt', 'r') as file_object:
    lines = [line.strip() for line in file_object]
""" Output:
["I've got a lovely bunch of coconuts", 'There they are, all standing in a row']
"""

""" Input:
8, 11, 28, 19
21, 28, 29, 27
3, 19, 12, 9
30, 30, 4, 4
14, 10, 2, 10
16, 12, 26, 22
15, 26, 11, 11
20, 7, 8, 28
3, 12, 5, 30
17, 6, 23, 1
"""
with open('values.csv', 'r') as file_object:
    rows = [row.split(',') for row in file_object]
""" Output:
[['8', ' 11', ' 28', ' 19\n'], ['21', ' 28', ' 29', ' 27\n'], ['3', ' 19', ' 12', ' 9\n'], ['30', ' 30', ' 4', ' 4\n'],
 ['14', ' 10', ' 2', ' 10\n'], ['16', ' 12', ' 26', ' 22\n'], ['15', ' 26', ' 11', ' 11\n'], ['20', ' 7', ' 8', ' 28\n'],
 ['3', ' 12', ' 5', ' 30\n'], ['17', ' 6', ' 23', ' 1\n']]
"""
with open('values.csv', 'r') as file_object:
    rows = [[int(value.strip()) for value in row.split(',')] for row in file_object]
"""
[[8, 11, 28, 19], [21, 28, 29, 27], [3, 19, 12, 9], [30, 30, 4, 4], [14, 10, 2, 10],
 [16, 12, 26, 22], [15, 26, 11, 11], [20, 7, 8, 28], [3, 12, 5, 30], [17, 6, 23, 1]]
"""

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

# Alternate way-------------------
import sys, csv

test_file = sys.argv[1]

total1 = 0
total2 = 0
total3 = 0
total4 = 0
row_count = 0

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file)
    for num1, num2, num3, num4 in reader:
        row_count += 1
        total1 += int(num1)
        total2 += int(num2)
        total3 += int(num3)
        total4 += int(num4)

print("{} {} {} {}".format(total1/row_count, total2/row_count, total3/row_count, total4/row_count))

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