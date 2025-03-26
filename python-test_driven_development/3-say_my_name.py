#!/usr/bin/python3
"""
This module contains a function that prints a person's name in the format:
'My name is <first_name> <last_name>'
"""

def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'

    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person, optional.

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")

