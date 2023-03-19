def avg(n1, n2):
    """Return average of two numbers
    Return a message is a non-number is passed"""
    try:
        return (n1 + n2) / 2
    except TypeError:
        return "Please use two numbers as parameters"
"""
-------------------------------------------------
"""

def odds_or_evens(my_bool, nums):
    """Returns all the odd or even numbers from a list"""
    return_list = []
    for num in nums:
        if my_bool:
            if num % 2 == 0:
                return_list.append(num)
        else:
            if num % 2 != 0:
                return_list.append(num)

    return return_list
"""
-------------------------------------------------
"""

def search_list(my_list, search_word):
    """Search for item in a list
    Return: index if found, -1 if not"""
    for word in my_list:
        if word.lower() == search_word.lower():
            return my_list.index(word)
    return -1

"""
-------------------------------------------------
"""
import csv

mlb_data = "student_folder/.exercises/mlb_data.csv"


def best_team(file):
    """Read a CSV of baseball data.
    Return: team name with the most wins"""
    with open(file, "r") as input_file:
        most_wins = 0
        team_name = ""
        reader = csv.reader(input_file)
        next(reader)
        for Tm, Lg, G, W, L in reader:
            if int(W) > most_wins:
                most_wins = int(W)
                team_name = Tm
    return team_name
"""
-------------------------------------------------
"""

def is_palindrome(word):
    """
    inputted word is checked if it is a palindrome
    (letters of the word are the same forward and reverse)
    splitting = [start:end:step] (-1 reverses)(::# does the full list)
    Returns: true or false if it is/is not a palindrome
    """
    if word[::-1] == word:
        return True
    return False
"""
-------------------------------------------------
"""

numbers = ((1, 2), (3, 4), (5, 6), (7, 8))
numbers2 = ((1, 2), (3, 0), (5, 6), (7, 8))

if (any((4) in element for element in numbers)):
  print("\nThe tuple called 'numbers' contains a '4'.")
else:
  print("\nThe tuple called 'numbers' does not contain a '4'.")

if (any((4) in element for element in numbers2)):
  print("\nThe tuple called 'numbers2' contains a '4'.")
else:
  print("\nThe tuple called 'numbers2' does not contain a '4'.")

"""
-------------------------------------------------
"""
jobs = ('doctor', 'dentist', 'musician', 'veterinarian', 'computer scientist', 'lawyer', 'electrician')
jobs_sorted = sorted(jobs, key = len, reverse = True)
print(jobs_sorted)
"""
-------------------------------------------------
"""
# range_value = range(start_value, end_value, increment_value)
range2 = tuple(range(5, 20, 3))
print(range2)
"""
-------------------------------------------------
"""
toys = ('bicycle', 'train', 'doll', 'teddy bear', 'kite', 'ball', 'video game set')

toys_list = [toys[index] for index in range(0, len(toys), 2)]
toys_every_other = tuple(toys_list)

print("Every Other Toy in the Tuple 'toys':", toys_every_other)
"""
-------------------------------------------------
"""
panel_prod_numbers = ('pan14GEtr', 'pan14GEf', 'pan14GEm', 'pan14G9Rf', 'pan14GR', 'pan14MPb', 'pan14MPrg', )
print("Sorted Panel Product Numbers by Element Length (ascending):", tuple(sorted(panel_prod_numbers, key = len)))
"""
-------------------------------------------------
"""
"""
We use mapping to apply a function or expression to every element in an iterable.
We use lambda() to create anonymous functions which can be applied to any number of iterables by,
for instance, using map().
"""
"""
We can use the map function to apply an expression (such as a function)
to elements in one or more iterables, such as tuples.
"""
# mapped_result = map(expression, iterable1, iterable2, ...)
def times_10(data):
  return(data * 10)
numbers = (9, 5, 3, 11, 14, 9, 7, 2)
numbers_times_10 = tuple(map(times_10, numbers))
print(numbers_times_10)
"""
-------------------------------------------------
"""
shirt_prices = (22.99, 28.99, 40.99, 38.99)

def inflation_increase(element):
  return(element * 1.14)

rounded_new_shirt_prices_list = []
for element in list(map(inflation_increase, shirt_prices)):
  rounded_new_shirt_prices_list.append(round(element, 2))

new_shirt_prices = tuple(rounded_new_shirt_prices_list)
print("New Graphic Shirt Prices:", new_shirt_prices)
"""
-------------------------------------------------
"""
school_abbreviations = ('PU', 'SU', 'HU', 'MIT')

abbreviations_broken_up = tuple(map(tuple, school_abbreviations))
print("School Abbreviations Broken Up:", abbreviations_broken_up)
"""
-------------------------------------------------
"""
"""
The lambda function is a function without a name, known as an anonymous function.
Using the lambda function, we can apply one expression to any number of iterables.

Use a lambda function to multiply each value in tuple numbers by 10.
Contain the output in tuple numbers_times_10_2, then print the tuple.
"""
numbers_times_10_2 = tuple(map(lambda element: element * 10, numbers))
print(numbers_times_10_2)
"""
-------------------------------------------------
"""
gas_prices = (4.09, 4.21, 3.99, 4.01)
print("Gas Prices before Inflation:", gas_prices)
"""
-------------------------------------------------
"""
ages = (65, 64, 66, 90, 84, 59, 70, 68)

qualified_65 = tuple(filter(lambda element: element >= 65, ages))
print("The following ages are 65 years or older, and therefore qualify:", qualified_65)
"""
-------------------------------------------------
"""
"""
The filter() function takes in two arguments, a function and an iterable (such as a tuple).

We can use the filter function to pull elements from an iterable, such as a tuple.
Where iterable may represent a specified tuple, we can use a function to filter
its data as shown below.
"""
# filtered_value = filter(function_name, iterable)
greetings = ("Hey", "Hello", "What's up?", "How are you?")

def filter_Hs(greeting):
  if greeting.startswith('H'): return True
  else: return False
all_H_greetings = tuple(filter(filter_Hs, greetings))

print("All Greetings:", greetings)
print("Greetings Beginning with 'H':", all_H_greetings)
"""
-------------------------------------------------
"""
factors_100 = (1, 2, 4, 5, 7, 10, 20, 22, 25, 50, 100)
print("Factors of 100 (incorrect) in Tuple 'factors_100':", factors_100)

factors_100 = tuple(filter(lambda element: (100 % element == 0), factors_100))
print("Factors of 100 (corrected) in Tuple 'factors_100':", factors_100)
"""
-------------------------------------------------
"""
random_values = ('argh', 'peanut', 16, 64, 'ice', 6, 'knife', 'spoon', 400)
factor_of_4 = tuple(filter(lambda element: type(element) == int and element % 4 == 0, random_values))
print("Values in Tuple 'random_values' with a Factor of 4:", factor_of_4)
"""
-------------------------------------------------
"""
image_names = ('potato.png', 'oatmeal.jpg', 'watermelon.png', 'broccoli.png', 'mango.jpg', 'beans.PNG', 'onions.JPG')

def filter_pngs(image_name):
  if image_name.endswith('.png'): return True
  else: return False
all_pngs = tuple(filter(filter_pngs, image_names))

print("All .png Image Names:", all_pngs)
"""
-------------------------------------------------
"""