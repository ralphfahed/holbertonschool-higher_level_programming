#!/usr/bin/python3
"""
BaseGeometry class with area and integer_validator methods
"""

class BaseGeometry:
    """
    BaseGeometry defines geometry-related methods.
    """

    def area(self):
        """
        Raises an Exception since area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the value (used in error messages).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
