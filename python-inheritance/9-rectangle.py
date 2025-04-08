#!/usr/bin/python3
'''
Module: Rectangle Class

This module defines a Rectangle class that inherits from the BaseGeometry class.

The Rectangle class has:
- Private attributes: width and height
- Methods for:
  - Validating integer inputs using integer_validator
  - Calculating the area of the rectangle
  - Returning a string representation of the rectangle

Classes:
    Rectangle (BaseGeometry): A class that represents a rectangle and its associated operations.
'''

from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    '''
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes the rectangle with width and height.
        area(self): Returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle in the format "[Rectangle] width/height".
    '''
    
    def __init__(self, width, height):
        '''
        Initializes the rectangle with width and height, validating them.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation in the format "[Rectangle] width/height".
        '''
        return f"[Rectangle] {self.__width}/{self.__height}"
