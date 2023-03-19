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
