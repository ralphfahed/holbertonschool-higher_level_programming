#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square.

        Returns:
            The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print("")  # Print an empty line if size is 0
            return

        for i in range(self.__size):  # Loop through the number of rows
            print("#" * self.__size)  # Print '#' repeated size times
