#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (which are cast to integers).

    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number, default is 98.

    Returns:
        int: The sum of a and b after converting them to integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # Convert float to int before addition
    a = int(a)
    b = int(b)
    return a + b
