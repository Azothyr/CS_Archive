class Course:
    def __init__(self, number=None, name=None, credit_hour=0.0, grade=0.0):
        if not isinstance(number, int):
            raise ValueError("Course number must be an integer")
        if not isinstance(name, str):
            raise ValueError("Course name must be a string")
        if not isinstance(credit_hour, float) or credit_hour < 0:
            raise ValueError("Credit hour must be a non-negative float")
        if not isinstance(grade, float) or grade < 0 or grade > 4:
            raise ValueError("Grade must be a float between 0.0 and 4.0")
        self._number = number
        self._name = name
        self._credit_hour = credit_hour
        self._grade = grade

    def number(self):
        return self._number

    def name(self):
        return self._name

    def credit_hr(self):
        return self._credit_hour

    def grade(self):
        return self._grade

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self._grade * other
        raise TypeError("Unsupported operand type for *: 'Course' and '{}'".format(type(other).__name__))

    def __str__(self):
        return f"{self._name} Grade: {self._grade} Credit Hours: {self._credit_hour}"

    def __eq__(self, other):
        if isinstance(other, Course):
            return self._number == other._number
        return False

    def __lt__(self, other):
        if isinstance(other, Course):
            return self._number < other._number
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Course):
            return self._number <= other._number
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Course):
            return self._number > other._number
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Course):
            return self._number >= other._number
        return NotImplemented
