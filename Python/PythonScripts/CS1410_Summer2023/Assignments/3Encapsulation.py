# In-Class activity module 4
"""
class StudentQuiz:
    def __init__(self, score=0):
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError(f"Error: Score must be between 0 and 100 to be valid")
        self._score = score
        return score


    # Other way to implement get;set;
    def get_score(self):
        return self._score

    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError(f"Error: Score must be between 0 and 100 to be valid")
        self._score = score
        return score

    score = property(get_score, set_score)



my_quiz = StudentQuiz()
# valid quiz scores are between 0 and 100
my_quiz.score = 95
print(my_quiz.score)
my_quiz.score = -5
print(my_quiz.score)
"""


class Country:
    def __init__(self, name, capital, population, continent):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent


country_parameters = ['_name', '_capital', '_population', '_continent']
my_country = Country('France', 'Paris', 67081000, 'Europe')
for parameter in country_parameters:
    value = getattr(my_country, parameter)
    print(value)
print()


class Artist:
    def __init__(self, name, medium, style, famous_artwork):
        self.__name = name
        self.__medium = medium
        self.__style = style
        self.__famous_artwork = famous_artwork


artist_parameters = ['_Artist__name', '_Artist__medium', '_Artist__style', '_Artist__famous_artwork']
my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')
for parameter in artist_parameters:
    value = getattr(my_artist, parameter)
    print(value)
print()


class BankAccount():
    def __init__(self):
        self._checking = 0
        self._savings = 0

    def get_checking(self):
        return self._checking

    def set_checking(self, new_value):
        self._checking = new_value

    def get_savings(self):
        return self._savings

    def set_savings(self, new_value):
        self._savings = new_value


my_account = BankAccount()
my_account.set_checking(523.48)
print(my_account.get_checking())
my_account.set_savings(386.15)
print(my_account.get_savings())


class Dancer:
    def __init__(self, name, nationality, style):
        self._name = name
        self._nationality = nationality
        self._style = style

    def get_name(self):
        return self._name

    def set_name(self, new_value):
        self._name = new_value

    def get_nationality(self):
        return self._nationality

    def set_nationality(self, new_value):
        self._nationality = new_value

    def get_style(self):
        return self._style

    def set_style(self, new_value):
        self._style = new_value

    name = property(get_name, set_name)
    nationality = property(get_nationality, set_nationality)
    style = property(get_style, set_style)


class Cyclist:
    def __init__(self, name, nationality, nickname):
        self._name = name
        self._nationality = nationality
        self._nickname = nickname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        self._name = new_value

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, new_value):
        self._nationality = new_value

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, new_value):
        self._nickname = new_value
