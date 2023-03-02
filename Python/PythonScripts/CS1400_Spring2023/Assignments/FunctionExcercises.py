def avg(n1, n2):
    """Return average of two numbers
    Return a message is a non-number is passed"""
    try:
        return (n1 + n2) / 2
    except TypeError:
        return "Please use two numbers as parameters"


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


def search_list(my_list, search_word):
    """Search for item in a list
    Return: index if found, -1 if not"""
    for word in my_list:
        if word.lower() == search_word.lower():
            return my_list.index(word)
    return -1


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
