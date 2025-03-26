#!/usr/bin/python3

def add_integer(a, b=98):
    """Adds two integers, converting floats to integers first.

    Args:
        a: The first number (must be an int or float).
        b: The second number (must be an int or float, default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)

    return a + b
