"""
import tech # imports from tech.py in the same directory as this file


my_phone = tech.Phone("Pixel 5", "sage", 128)
my_laptop = tech.Laptop("MacBook Pro", 15, 256)

print(my_phone)
print(my_laptop)
"""


class Band:
    def __init__(self, name, genre, members):
        self.name = name
        self.genre = genre
        self.members = members

    def __str__(self):
        return f"{self.name} is a {self.genre} band."

    def __repr__(self):
        return f"Band({self.name}, {self.genre}, {self.members})"


dead = Band('The Grateful Dead', 'rock\'n roll', ['Jerry', 'Bob', 'Mickey', 'Bill', 'Phil', 'Pigpen'])

print(dead)
print(repr(dead))


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f"{self.name}, {self.breed} "


dogs = []
dog_list = ['Marceline', 'German Shepherd',
            'Cajun', 'Belgian Malinois',
            'Daisy', 'Border Collie',
            'Rocky', 'Golden Retriever',
            'Bella', 'Irish Setter']
for name, breed in zip(dog_list[::2], dog_list[1::2]):
    dogs.append(Dog(name, breed))

print(dogs)

"""
# exercise4.py
from library import Library
from book import Book


library = Library()
book1 = Book('Three Musketeers', 'Alexandre Dumas', 'fiction')
book2 = Book('The Count of Monte Cristo', 'Alexandre Dumas', 'fiction')
book3 = Book('Educated', 'Tara Westover', 'nonfiction')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.sort_books()

print(library.books)
print(library.fiction)
print(library.nonfiction)
print(library.search_author('Alexandre Dumas'))
print(library.search_author('Herman Melville'))
print(library.search_title('Educated'))
print(library.search_title('Moby Dick'))



# library.py
class Library:
    def __init__(self):
        self.books = []
        self.fiction = []
        self.nonfiction = []

    def add_book(self, book):
        '''Takes a Book object and adds it to self.books'''
        self.books.append(book)

    def search_title(self, title):
        '''Takes a string and returns a Boolean'''
        has_book = False
        for book in self.books:
            if title.lower() == book.title.lower():
                has_book = True
        return has_book

    def search_author(self, author):
        '''Takes a string and returns a list of Book objects'''
        author_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                author_books.append(book)
        return author_books

    def sort_books(self):
        '''Helper method for sort_fiction and sort_nonfiction'''
        self.fiction = self.sort_fiction()
        self.nonfiction = self.sort_nonfiction()

    def sort_fiction(self):
        '''Return list of Book objects where the genre is fiction'''
        fiction_books = []
        for book in self.books:
            if book.genre.lower() == 'fiction':
                fiction_books.append(book)
        return fiction_books

    def sort_nonfiction(self):
        '''Return list of Book objects where the genre is nonfiction'''
        nonfiction_books = []
        for book in self.books:
            if book.genre.lower() == 'nonfiction':
                nonfiction_books.append(book)
        return nonfiction_books


# book.py
class Book:
  def __init__(self, title, author, genre):
    self.author = author
    self.title = title
    self.genre = genre
    
  def __repr__(self):
    return f'Book({self.title}, {self.author}, {self.genre})'
"""


# exercise5.py
from item import Item
from shopping_cart import ShoppingCart

item1 = Item('milk', 1.5, 1)
item2 = Item('apple', 5, 0.75)
item3 = Item('bread', 2, 2.25)
cart = ShoppingCart()

cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

print(cart.get_total())  # 9.75
print(cart.get_num_items())  # 3
print(cart)  # The cart has 3 items for a total of $9.75
print(cart.get_items())  # [Item(milk, 1.5, 1, 1.5), Item(apple, 5, 0.75, 3.75), Item(bread, 2, 2.25, 4.5)]


# item.py
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal = 0

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}, {self.subtotal})"

    def calculate_subtotal(self):
        self.subtotal = self.price * self.quantity

    def get_subtotal(self):
        return self.subtotal


# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item):
        self.items.append(item)
        self.calculate_total()

    def calculate_total(self):
        self.total = 0
        for item in self.items:
            item.calculate_subtotal()
            self.total += item.get_subtotal()

    def get_total(self):
        return self.total

    def get_num_items(self):
        return len(self.items)

    def get_items(self):
        return self.items

    def __str__(self):
        return f'The cart has {self.get_num_items()} items for a total of ${self.total}'
