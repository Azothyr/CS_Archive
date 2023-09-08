oregon_cities = ["Portland", "Salem"]
oregon_cities2 = ["Eugene"]

nebraska_cities = {"Omaha", "Lincoln"}
nebraska_cities2 = {"Nebraska City"}

iowa_cities = {
  "Capital" : "Des Moines",
  "Most Fun City" : "Iowa City"
  }
iowa_cities2 = {
  "Most Beautiful City" : "Cedar Rapids"
}

oregon = tuple(oregon_cities) + tuple(oregon_cities2)
print("All Oregon Cities:", oregon)

nebraska = tuple(nebraska_cities) + tuple(nebraska_cities2)
print("All Nebraska Cities:", nebraska)

def merge_dicts(dict1, dict2):
  return(dict1.update(dict2))
merge_dicts(iowa_cities, iowa_cities2)
iowa_list = []
for element in iowa_cities:
  iowa_cities_item_to_subtuple = (element, iowa_cities[element])
  iowa_list.append(iowa_cities_item_to_subtuple)
iowa = tuple(iowa_list)
print("All Iowa Cities:", iowa)
"""
-------------------------------------------------
"""
subtuples = ((10, 1), (0, 4), (-8, 100), (40, 9))

subtuple_maxs = tuple([max(element) for element in subtuples])
print("Maximum Value in each Sub Tuple in Tuple 'subtuples':", subtuple_maxs)
"""
-------------------------------------------------
"""
subtuples = ((10, 1), (0, 4), (-8, 100), (40, 9))

subtuple_index0_values = []
for (element1, element2) in subtuples:
  subtuple_index0_values.append(element1)
subtuple_index0_min = min(subtuple_index0_values)
print("Minimum Value of Index Value 0 in each sub tuple:", subtuple_index0_min)
"""
-------------------------------------------------
"""
"""
When we refer to zipping tuples, we mean that we are using the zip cus_funcs to form a collection
of iterable element values pulled from two or more iterables, such as a tuple.
a = ('dog', 'cat')
b = (55, 35)
a_b_zipped = (('dog', 55), ('cat', 35))
"""
# zipped_iterables = zip(iterable1, iterable2, ....)
# unzipped_iterable1, unzipped_iterable2, ... = zip(*iterable)
meals = ('breakfast', 'lunch', 'dinner')
meal_times = ('8 am', '12 pm', '6 pm')
meal_info = tuple(zip(meals, meal_times))
print(meal_info)
meals2, meal_times2 = zip(*meal_info)
print(meals2, "\n", meal_times2)
"""
-------------------------------------------------
"""
random_nums1 = (1, 10, 2, 448, 9)
random_nums2 = (50, 30, 20, 48, 49)

print("Is random_nums1 less than random_nums2 (only comparing Index Value 0)? (T/F):", random_nums1 < random_nums2)
## compares only the first element with the same data type, not all elements

comparison = all(random_num1 < random_num2 for random_num1, random_num2 in zip(random_nums1, random_nums2))
## compares all element values in both tuples
print("Is random_nums1 less than random_nums2? (T/F):", comparison)
"""
-------------------------------------------------
"""
student_grades = (('MaKayden', 82), ('Nyron', 'N/A'), ('Taylor', 80), ('Noel', 'N/A'))

def remove_NA(data):
  data_list = [list(subtuple) for subtuple in data]
  updated_data = ()
  for subtuple in data_list:
    if 'N/A' in subtuple:
      index_value = subtuple.index('N/A')
      subtuple[index_value] = 'Test not taken yet'
      updated_data += tuple(subtuple),
    else:
      updated_data += tuple(subtuple),
  return (updated_data)


print("Updated Student Grades:", remove_NA(student_grades))
"""
-------------------------------------------------
"""
values = ((14, 5), (9, 8), (144, 983), (7000, 1), (54, 54))

def sort_values(data):
  sorted_values = tuple(sorted(data, key = lambda subtuple : sum([len(str(element)) for element in subtuple])))
  return(sorted_values)
print('Sorted Values:', sort_values(values))
"""
-------------------------------------------------
"""
dividend = (10, 100, 1000, 10000)
divisor = (5, 50, 500, 5000)

def find_quotient(tuple1, tuple2):
  quotient = tuple((tuple1_element / tuple2_element) for tuple1_element, tuple2_element in zip(tuple1, tuple2))
  return(quotient)

print(find_quotient(dividend, divisor))
"""
-------------------------------------------------
"""
numbers = (8, 5, 9, 14, 22)

def find_adj_products(data):
  numbers_adj_prod = tuple(left_element * right_element for left_element, right_element in zip(data, data[1:]))
  return (numbers_adj_prod)


print(find_adj_products(numbers))
"""
-------------------------------------------------
"""
tuple_pairs = ((4, 5), (6, 14), (100, 40), (0, 83))

def find_pair_diff(data):
  pair_diff = [abs(subtuple[-1] - subtuple[0]) for subtuple in data]
  return (tuple(pair_diff))


def find_max_diff(data):
  max_diff_subtuple = max(data, key=lambda subtuple: abs(subtuple[-1] - subtuple[0]))
  max_diff = max(abs(subtuple[-1] - subtuple[0]) for subtuple in data)
  return (max_diff_subtuple, max_diff)


print(find_pair_diff(tuple_pairs))
print(find_max_diff(tuple_pairs))
"""
-------------------------------------------------
tuple packing
"""
dog = 'cat'
cat = 'dog'

dog, cat = cat, dog

print("Value of variable 'dog':", dog)
print("Value of variable 'cat':", cat)
"""
-------------------------------------------------
"""
midterm_grades = (('Mackenzie', 89), ('Nakai', 92), ('Dante', 85), ('Max', 96), ('Hadja', 98), ('Jayda', 90))

def find_avg_grade(midterm_grades):
    total_grade = 0
    num_students = len(midterm_grades)
    for name, grade in midterm_grades:
        total_grade += grade
    avg_grade = total_grade / num_students
    return round(avg_grade, 2)

print(find_avg_grade(midterm_grades))
"""
-------------------------------------------------
"""
values = ((9,4), (3,6), (4,9), (3,4))

def find_unique_tuple_freq(data):
  unique_tuple_freq = len(list(set(tuple(sorted(subtuple)) for subtuple in list(data))))
  return(unique_tuple_freq)

print(find_unique_tuple_freq(values))
"""
-------------------------------------------------
"""
rating_key = ('Food', 'Release year', 'Dish type', 'Dish weight', 'Dish taste', 'Dish surprise', 'Cost value', 'Rating')

sampler = (2019, 'Appetizer', 8, 4, 0, 2, 4.375)
antipasto_platter = (2022, 'Appetizer', 8, 4, 1, 2, 4.6875)
zuchinni_sticks = (2022, 'Appetizer', 4, 3, 0, 5, 3.75)
garlic_bread = (2016, 'Appetizer', 5, 6, 0, 4, 4.6875)
bruschetta_trio = (2016, 'Appetizer', 7, 8, 2, 8, 7.8125)
stuffed_portabella = (2018, 'Appetizer', 5, 4, 1, 8, 5.625)
eggplant_parm_sandwich = (2020, 'Sandwich', 8, 4, 0, 6, 5.625)
chick_n_caesar_wrap = (2018, 'Sandwich', 7, 10, 1, 9, 8.4375)
italian_deli = (2016, 'Sandwich', 10, 7, 0, 10, 8.4375)
classic_burger = (2021, 'Sandwich', 9, 7, 0, 10, 8.125)
meatball_on_a_ciabatta = (2016, 'Sandwich', 9, 6, 0, 7, 6.875)
chick_n_parmesan = (2016, 'Entree', 9, 7, 0, 6, 6.875)
eggplant_parmesan = (2018, 'Entree', 7, 4, 0, 6, 5.3125)
lasagna = (2019, 'Entree', 8, 10, 2, 9, 9.0625)
spaghetti_meatballs = (2019, 'Entree', 8, 8, 0, 10, 8.125)
tiramisu = (2016, 'Dessert', 3, 9, 2, 10, 7.5)
cannoli = (2019, 'Dessert', 3, 9, 1, 2, 4.6875)
chocolate_cake = (2019, 'Dessert', 4, 8, 0, 6, 5.625)
chocolate_almond_croissant = (2022, 'Dessert', 5, 10, 2, 4, 6.5625)

all_menu_items = (sampler, antipasto_platter, zuchinni_sticks, garlic_bread, bruschetta_trio, stuffed_portabella, eggplant_parm_sandwich, chick_n_caesar_wrap, italian_deli, classic_burger, meatball_on_a_ciabatta, chick_n_parmesan, eggplant_parmesan, lasagna, spaghetti_meatballs, tiramisu, cannoli, chocolate_cake, chocolate_almond_croissant)
print('All Menu Items:', all_menu_items)

menu_item_ratings = tuple(item[-1] for item in all_menu_items)
print('Menu Item Ratings:', menu_item_ratings)

average_menu_item_rating = round(sum(menu_item_ratings) / len(menu_item_ratings), 4)
print('Average Menu Item Rating:', average_menu_item_rating)

menu_items = ('Sampler', 'Antipasto Platter', 'Zuchinni Sticks', 'Garlic Bread', 'Bruschetta Trio', 'Stuffed Portabella', 'Eggplant Parm Sandwich', "Chick'n Caesar Wrap", 'Italian Deli', 'Classic Burger', 'Meatball on a Ciabatta', "Chick'n Parmesan", 'Eggplant Parmesan', 'Lasagna', 'Spaghetti Meatballs', 'Tiramisu', 'Cannoli', 'Chocolate Cake', 'Chocolate Almond Croissant')

print("Menu Items Ranked In Order from Best to Worst:\n")
for counter_value, (menu_item, menu_item_rating) in enumerate(sorted(zip(menu_items, menu_item_ratings), key = lambda element: element[1], reverse = True), 1):
  print(counter_value, ":", menu_item, "with a rating of:", menu_item_rating, ".")
"""
-------------------------------------------------
"""
