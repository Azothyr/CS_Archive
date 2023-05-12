class CelestialBody:
    """Represents a celestial body"""

    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons

    def compared_to_earth(body):
        """Determines the size of a celestial
        body relative to Earth using diameter"""
        earth = 12756.3
        relative_size = body.diameter / earth
        return relative_size


planet = CelestialBody("Jupiter", 142984, 778360000, 79)
print(CelestialBody.compared_to_earth(planet))


class CelestialBody:
    """Represents a celestial body"""

    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons

    @staticmethod
    def closer_to_sun(planet1, planet2):
        if planet1.distance < planet2.distance:
            return planet1.name
        else:
            return planet2.name


mercury = CelestialBody("Mercury", 4879.4, 57909000, 0)
venus = CelestialBody("Venus", 12103.6, 108160000, 0)
print(CelestialBody.closer_to_sun(mercury, venus))


class CelestialBody:
    """Represents a celestial body"""

    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons

    @classmethod
    def make_earth(cls):
        return CelestialBody('Earth', 12756.3, 149600000, 1)


my_planet = CelestialBody.make_earth()
print(my_planet.name)
print(my_planet.distance)
print(my_planet.diameter)
print(my_planet.moons)


class Library:
    """List of available books and list of books on loan"""

    def __init__(self):
        self.available = []
        self.on_loan = []

    def add_books(self, titles):
        """Add books to the Library's available list"""
        for book in titles:
            self.available.append(book)

    def borrow_book(self, title):
        """Remove book from available to on loan"""
        self.available.remove(title)
        self.on_loan.append(title)

    def return_book(self, title):
        """Remove book from on loan to available"""
        self.on_loan.remove(title)
        self.available.append(title)


my_library = Library()
my_library.add_books(["Four Seasons", "Say Nothing", "Milkman", "Harry Potter and the Order of the Phoenix"])
print(my_library.available)

my_library.borrow_book("Harry Potter and the Order of the Phoenix")
my_library.borrow_book("Say Nothing")
print(my_library.available)
print(my_library.on_loan)


class Subway:
    fare = 2.4

    def __init__(self):
        self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]
        self.current_stop = "Alewife"
        self.direction = "south"
        self.passengers = 0
        self.total_fares = 0

    def board(self, boarding):
        self.passengers += boarding
        self.calculate_fares(boarding)

    def disembark(self, leaving):
        if leaving <= self.passengers:
            self.passengers -= leaving
        else:
            self.passengers = 0

    def advance(self):
        self.stops = ["Alewife", "Davis", "Porter", "Harvard", "Central", "Kendall"]

        if self.current_stop == "Alewife" and self.direction == "north":
            self.direction = "south"
        if self.current_stop == "Kendall" and self.direction == "south":
            self.direction = "north"

        if self.direction == "north":
            self.stops.reverse()

        self.current_stop = self.stops[self.stops.index(self.current_stop) + 1]

    def distance(self, desired_stop):
        current_stop = int(self.stops.index(self.current_stop))
        distance = abs(current_stop - int(self.stops.index(desired_stop)))
        return distance

    def calculate_fares(self, amount):
        self.total_fares += amount * self.fare

    @classmethod
    def change_fare(cls, new_fare):
        Subway.fare = new_fare


subway = Subway()
subway.passengers = 220
subway.board(45)
print(subway.passengers)

subway.board(55)
print(subway.total_fares)

subway.passengers = 113
subway.disembark(23)
print(subway.passengers)

subway.current_stop = 'Kendall'
subway.direction = 'south'
subway.advance()
print(subway.current_stop)
print(subway.direction)

subway.current_stop = 'Porter'
subway.direction = 'south'
subway.advance()
print(subway.current_stop)
print(subway.direction)

subway.current_stop = "Davis"
print(subway.distance("Central"))

subway.change_fare(2.75)
print(Subway.fare)
print(subway.fare)
