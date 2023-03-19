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
When we refer to zipping tuples, we mean that we are using the zip function to form a collection
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
