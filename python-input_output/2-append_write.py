#!/usr/bin/python3
"""Module to append a string to a UTF-8  and return the number of char"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF-8) and returns the number of char

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
