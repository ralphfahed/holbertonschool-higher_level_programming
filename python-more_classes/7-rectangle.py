#!/usr/bin/python3

"""Module that defines a Rectangle class."""


class Rectangle:
    """Class that defines a rectangle with width and height properties."""

    # Public class attribute
    number_of_instances = 0
    # Public class attribute
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height
        # Increment the class attribute whenever a new instance is created
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        Ensures it is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        Ensures it is a non-negative integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        If width or height is 0, the perimeter is 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the string representation of rectangle with # characters."""
        if self.width == 0 or self.height == 0:
            return ""  # If either dimension is zero, return an empty string.
         # Ensure print_symbol is treated as a string
        symbol = str(self.print_symbol)
        # Create a row with width number of '#'
        row = symbol * self.width
        # Repeat the row 'height' times, and join them with newlines
        return "\n".join([row] * self.height)

    def __repr__(self):
        """Return a string representation of the rectangle to recreate it."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message when the instance is deleted."""
        print(f"Bye rectangle...")  # The message when deleted
        # Decrement the class attribute whenever an instance is deleted
        Rectangle.number_of_instances -= 1
