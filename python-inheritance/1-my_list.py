#!/usr/bin/python3
"""
This module defines the MyList class that inherits from list.
It includes a method print_sorted() that prints the list in ascending order.
"""

class MyList(list):
    """
    A class that inherits from list and adds a method for printing the sorted list.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).
        Does not modify the original list.
        """
        print(sorted(self))

