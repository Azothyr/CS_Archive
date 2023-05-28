class PracticeClass:
    pass


class Cat:
    def __init__(self):
        self.breed = "american shorthair"
        self.color = "black"
        self.name = "kiwi"


my_cat = Cat()
print(my_cat.breed, my_cat.color, my_cat.name)


class SuperHero:
    def __init__(self, name, secret_identity, powers):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers


spider_man = SuperHero("Spider-Man", "Peter Parker", ["superhuman strength", "superhuman speed", "superhuman reflexes",
                                                      "superhuman durability", "healing factor", "spider-sense alert",
                                                      "heightened senses", "wallcrawling"])
print(spider_man.name, spider_man.secret_identity, spider_man.powers)


class Observation:
    def __init__(self, date, temperature, elevation, penguins, precipitation=0.0):
        self.date = date
        self.temperature = temperature
        self.elevation = elevation
        self.precipitation = precipitation
        self.penguins = penguins


observation = Observation("October 26, 2019", -47, 329.4, 3, 0.7)
print(observation.date)
print(observation.temperature)
print(observation.elevation)
print(observation.precipitation)
print(observation.penguins)


class BigCat:
    genus = "panthera"

    def __init__(self, species, common_name, habitat):
        self.species = species
        self.common_name = common_name
        self.habitat = habitat


big_cat = BigCat("tigris", "tiger", ["asia"])
print(big_cat.species)
print(big_cat.common_name)
print(big_cat.habitat)
