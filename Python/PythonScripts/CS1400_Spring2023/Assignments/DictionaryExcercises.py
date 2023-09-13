import pprint

actor = {
    'first_name': 'Denzel',
    'last_name': 'Washington',
    'films': [
        ('Malcolm X', 1992),
        ('The Hurricane', 1999),
        ('Training Day', 2001),
        ('Fences', 2016)
    ],
    'oscars': [{
        'award': 'Best actor in a supporting role',
        'film': 'Glory',
        'year': 1990
    }, {
        'award': 'Best actor in a leading role',
        'film': 'Training Day',
        'year': 2002
    }]
}

pprint.pprint(actor)
"""
-------------------------------------------------
"""
import pprint

actor = {
  'first_name' : 'Denzel',
  'last_name' : 'Washington',
  'films' : [
    ('Malcolm X', 1992),
    ('The Hurricane',  1999),
    ('Training Day', 2001),
    ('Fences', 2016)
  ],
  'oscars' : [{
    'award' : 'Best actor in a supporting role',
    'film' : 'Glory',
    'year' : 1990
  }, {
    'award' : 'Best actor in a leading role',
    'film' : 'Training Day',
    'year' : 2002
  }]
}

oscars = actor['oscars']
for oscar in oscars:
  pprint.pprint(oscar.keys())
"""
-------------------------------------------------
"""
import pprint
import copy

actor = {
  'first_name' : 'Denzel',
  'last_name' : 'Washington',
  'films' : [
    ('Malcolm X', 1992),
    ('The Hurricane',  1999),
    ('Training Day', 2001),
    ('Fences', 2016)
  ],
  'oscars' : [{
    'award' : 'Best actor in a supporting role',
    'film' : 'Glory',
    'year' : 1990
  }, {
    'award' : 'Best actor in a leading role',
    'film' : 'Training Day',
    'year' : 2002
  }]
}

actor_copy = copy.deepcopy(actor)
actor_copy['films'][3] = ('Remember the Titans', 2000)

print(f'Actor: {id(actor["films"])}')
print(f' Copy: {id(actor_copy["films"])}')
"""
-------------------------------------------------
"""
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

msg = 'The watch you are looking for does not exist'
print(watches.get('Royal Oak', msg)) # if royal oaks is not there it will print the msg
"""
-------------------------------------------------
"""
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches.setdefault('Royal Oak', 'Audemars Piguet')
print(watches) # if royal oak is not there is will create it as a key and give it the value Audemars Piguet
"""
-------------------------------------------------
"""
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

print(watches.pop('Royal Oak', -1))
# pop will remove the key and items of royal oak, and will return the items of the key.
# if there is no key it will return -1
"""
-------------------------------------------------
"""
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

print(watches.popitem())
print(watches)
# The popitem() method does not take any parameters.
# It removes the last item in the dictionary and returns it as a tuple.
"""
-------------------------------------------------
We can avoid program crashes from popping a empty dictionary by checking the length first.
Len returns the amount of keys.
"""
def pop_item(d):
  if len(d) == 0:
    return -1
  else:
    return d.popitem()

watches = {}

print(pop_item(watches))
"""
-------------------------------------------------
The del statement deletes an item from a dictionary. 
Type del followed by the name of the dictionary, square brackets, 
and the key of the item to be removed.
you cannot specify an alternative return value with del
"""
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

print(del watches['Speedmaster'])
"""
-------------------------------------------------
As its name implies, the clear() method clears out a dictionary.
"""
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches.clear()
print(watches)
"""
-------------------------------------------------
update a dictionary
dictionary['key'] = new_value
"""
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches.update(Speedmaster='Swatch Group', Tank='Richemont')
print(watches)
"""
-------------------------------------------------
You can also use update() to combine one dictionary with another dictionary.
The dictionary passed as a parameter will be placed at the end of the other dictionary.
The update() method works with any iterable (list, dictionary, tuple, etc.),
so it can combine more than just two dictionaries.
"""
watches1 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches2 = [
  ['Calatrava', 'Patek Philippe'],
  ['Datejust', 'Rolex'],
  ['Royal Oak', 'Audemars Piguet']
]

watches1.update(watches2)
print(watches1)
"""
-------------------------------------------------
fromkeys() is a class method that creates a new dictionary. 
Pass the method an iterable, which will be used as the keys. 
Using this method means every value will be the same. 
The default value is None. 
You can pass fromkeys() an optional parameter which will be used in place of None.
"""
models = ['Speedmaster', 'Submariner', 'Tank']

watches1 = dict.fromkeys(models)
watches2 = dict.fromkeys(models, 'Manufacturer')

print(watches1)
print(watches2)
"""
-------------------------------------------------
the copy() method so that the dictionaries are independent of one another. 
A change to one dictionary should no longer affect the other.
"""
watches1 = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

watches2 = watches1.copy()
watches1['Submariner'] = 'Tudor'

print(watches1)
print(watches2)
"""
-------------------------------------------------
Like lists, the in operator returns a boolean if a key is found in a dictionary.
searching a dictionary with in is vastly more efficient than searching a list with in
this is due to dictionaries using hashing
The performance of a list is proportional to its length.
The performance of a dictionary is independent of its length
"""
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

print('Tank' in watches) # returns True
print('Cartier' in watches) # returns False because it only looks at keys
"""
-------------------------------------------------
can check for values with .values
"""
watches = {
  'Speedmaster' : 'Omega',
  'Submariner' : 'Rolex',
  'Tank' : 'Cartier'
}

values = watches.values()
print('Omega' in values)
"""
-------------------------------------------------
"""
nums = {
  1 : 'odd',
  2 : 'even',
  3 : 'odd',
  4 : 'even',
  5 : 'odd'
}
print(odds = {k:v for k, v in nums.items() if v == 'odd'})
"""
-------------------------------------------------
Find key from a value
"""
def find_key(dictionary, value):
  for k, v in dictionary.items():
    if v == value:
      return k
  return None


if __name__ == "__main__":
  example_dict = {
    1 : ['red', 'blue', 'green'],
    'Josh Jung' : (9, 10),
    3 : {0 : 0},
    9000 : 'impale mat a'
  }

  key = find_key(example_dict, (9, 10))
  print(key)
"""
-------------------------------------------------
takes a dictionary and a key and returns a dictionary where the specified key and associated value
are moved to the bottom of the dictionary. If the key is not in the dictionary, return the string:
The key is not in the dictionary
"""
def move_to_bottom(dictionary, key):
  if key in dictionary:
    value = dictionary.pop(key)
    dictionary.update({key: value})
    return dictionary
  else:
    return "The key is not in the dictionary"

if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

  print(move_to_bottom(example_dict, 4))
"""
-------------------------------------------------
swap key and values. Values are now keys, keys are now values.
"""
def swap(d):
  keys = d.keys()
  values = d.values()
  swapped_tuples = zip(values, keys)
  value_types = [type(elem) for elem in values]

  if type({}) in value_types or type([]) in value_types:
    return 'Cannot swap the keys and values for this dictionary'
  else:
    new_dict = dict(swapped_tuples)
    return new_dict


if __name__ == "__main__":
  example_dict = {
    1: 'one',
    2: 'two',
    3: (4, 5)
  }

  swapped = swap(example_dict)
  print(swapped)
"""
-------------------------------------------------
Return True if the given dictionary is a nested dictionary; return False if not. 
For the purposes of this exercise,a nested dictionary is any dictionary with a list,
tuple, or dictionary as a value.
"""
def is_nested(d):
  values = d.values()
  value_types = [type(elem) for elem in values]
  if type(()) in value_types or type([]) in value_types or type({}) in value_types:
    return True
  else:
    return False

if __name__ == "__main__":
  example_dict = {
    1 : (2, 3),
    4 : 'four',
    5 : 'five'
  }

  print(is_nested(example_dict))
"""
-------------------------------------------------
Same result
"""
def is_nested(dictionary):
  for value in dictionary.values():
    if isinstance(value, (dict, list, tuple)):
      return True
  return False

if __name__ == "__main__":
  example_dict = {
    1 : (2, 3),
    4 : 'four',
    5 : 'five'
  }

  print(is_nested(example_dict))
"""
-------------------------------------------------
takes two file paths. The functions opens each JSON file and returns a string stating:
The dictionaries are equal
Dictionary 1 is longer than dictionary 2
Dictionary 2 is longer than dictionary 1
Dictionary 1 and dictionary 2 have the same length
"""
import json


def compare(file1, file2):
  with open(file1) as f1, open(file2) as f2:
    dict1 = json.load(f1)
    dict2 = json.load(f2)

  if dict1 == dict2:
    return "The dictionaries are equal"
  elif len(dict1) > len(dict2):
    return "Dictionary 1 is longer than dictionary 2"
  elif len(dict1) < len(dict2):
    return "Dictionary 2 is longer than dictionary 1"
  else:
    return "Dictionary 1 and dictionary 2 have the same length"


if __name__ == "__main__":
  import sys

  file1 = sys.argv[1]
  file2 = sys.argv[2]

  print(compare(file1, file2))
"""
-------------------------------------------------
"""
"""
-------------------------------------------------
"""
"""
-------------------------------------------------
"""