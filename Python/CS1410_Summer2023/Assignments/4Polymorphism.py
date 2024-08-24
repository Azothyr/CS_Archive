import random


class Lottery:
    def shuffle(self):
        results = []
        for i in range(5):
            results.append(random.randint(1, 20))
        return results


class PowerBall(Lottery):

    def shuffle(self):
        results = []
        for i in range(6):
            results.append(random.randint(1, 99))
        return results


my_powerball = PowerBall()
print(my_powerball.shuffle())


class Airplane:
    def __init__(self, first_class, business_class, coach):
        self.first_class = first_class
        self.business_class = business_class
        self.coach = coach

    def total(self):
        return self.first_class + self.business_class + self.coach


class Train:
    def __init__(self, car1, car2, car3, car4, car5):
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3
        self.car4 = car4
        self.car5 = car5

    def total(self):
        return self.car1 + self.car2 + self.car3 + self.car4 + self.car5


def passengers(obj):
    print(f'There are {obj.total()} passengers on board.')


my_airplane = Airplane(1, 1, 1)
my_train = Train(1, 1, 1, 1, 1)
passengers(my_train)
passengers(my_airplane)


class Characters:
    def __init__(self, phrases):
        self.phrases = phrases

    def __lt__(self, other):
        return self.total_characters() < other.total_characters()

    def __gt__(self, other):
        return self.total_characters() > other.total_characters()

    def __eq__(self, other):
        return self.total_characters() == other.total_characters()

    def total_characters(self):
        return sum(len(phrase) for phrase in self.phrases)


sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

c1 = Characters(sample_phrases1)
c2 = Characters(sample_phrases2)
print(c1 > c2)  # prints 'True'
print(c1 < c2)  # prints 'False'
print(c1 == c1)  # prints 'True'


class Median:
    @staticmethod
    def calculate_median(a, b, c=None, d=None, e=None):
        numbers = [value for value in [a, b, c, d, e] if value is not None]
        numbers.sort()

        n = len(numbers)
        mid = n // 2

        if n % 2 == 0:
            median = (numbers[mid - 1] + numbers[mid]) / 2
        else:
            median = numbers[mid]

        return median


print(Median.calculate_median(1, 2, 3, 4))


"""
source_file = '/home/codio/workspace/code/polymorphism/text_1_exercise5.txt'
answer_file = '/home/codio/workspace/code/polymorphism/answer_exercise5.txt'

class Substitute:
  def __init__(self, source_file, answer_file):
    self.source_file = source_file
    self.answer_file = answer_file
    self.words = None
    
  def string_to_list(self):
    '''Read text file, turn it into a
    2D list of words for each line'''
    words = []
    with open(self.source_file, 'r') as file_object:
      lines = file_object.read().split('\n')
      for line in lines:
        words.append(line.split())
    self.words = words
    
  def list_to_string(self):
    '''Convert 2D list back into a 
    string with newline characters'''
    lines = []
    for line in self.words:
      lines.append(' '.join(line))
    string = '\n'.join(lines)
    self.words = string
  
  def swap_words(self):
    self.string_to_list()
    for line in self.words:
      for i in range(len(line)):
        if (i + 1) % 5 == 0:
          word = line[i]
          line[i] = 'HELLO'
    self.list_to_string()


class Stars(Substitute):
    def swap_words(self):
        self.string_to_list()
        for line in self.words:
            for i in range(len(line)):
                if (i + 1) % 3 == 0:
                    word = line[i]
                    amount = 0
                    for letter in word:
                        amount += 1
                    line[i] = '*' * amount
        self.list_to_string()

s = Stars(source_file, answer_file)
s.swap_words()
print(s.words)
"""