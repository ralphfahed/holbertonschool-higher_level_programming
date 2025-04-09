#!/usr/bin/python3
'''
Module: Square Class
Defines a Square class that inherits from Rectangle.
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    A class representing a square, inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Initializes the square.
        area(self): Returns the area of the square.
        __str__(self): Returns a string representation of the square.
    '''

    def __init__(self, size):
        '''
        Initializes a square with size, validating it.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size <= 0.
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''
        Returns the area of the square.

        Returns:
            int: The area (size * size).
        '''
        return self.__size ** 2

    def __str__(self):
        '''
        Returns the string representation of the square.

        Returns:
            str: [Square] size/size
        '''
        return f"[Square] {self.__size}/{self.__size}"

