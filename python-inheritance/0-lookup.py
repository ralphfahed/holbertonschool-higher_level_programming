#!/usr/bin/python3
"""
This module provides a function that returns a list of all available
attributes and methods of a given object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing names of the attributes and methods of the object.
    """
    return dir(obj)
