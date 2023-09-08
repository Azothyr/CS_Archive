"""
Project: Binary Search Tree
Author: Zac Peterson
Course: CS 2420
Date: 6/1/2023

Description:

Lessons Learned:
"""
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    """
    Encapsulate letter,count pair as a single entity.

    Relational methods make this object comparable
    using built-in operators.
    """
    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'


def make_tree():
    """
    A helper cus_funcs to build the tree.
    """
    bst = BST()
    ignore_chars = set(whitespace + punctuation)

    with open('around-the-world-in-80-days-3.txt', 'r') as file:
        for line in file:
            for char in line:
                char = char.lower()
                if char not in ignore_chars:
                    try:
                        pair = bst.find(Pair(char))  # Try to find the character in the tree
                        pair.count += 1  # If it's found, increment the count
                    except ValueError:  # If the character is not in the tree, ValueError is raised
                        bst.add(Pair(char))  # If it's not found, add a new pair to the tree
    return bst


def main():
    """
    Program kicks off here.
    """
    tree = make_tree()
    print(f"Empty: {tree.is_empty()}\nSize: {tree.size()}\nHeight: {tree.height()}\n")
    tree.print_tree()
    tree.print_tree("preorder")
    tree.print_tree("postorder")


if __name__ == "__main__":
    main()
