#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""  # Initialize an empty string

    for char in text:  # Loop through each character in text
        if char == " " and result and result[-1] in ".?:":
            continue  # Skip space right after ., ?, :

        result += char  # Add character to result

        if char in ".?:":
            result += "\n\n"  # Add two new lines after ., ?, :

    # Ensure the final output includes the correct number of newlines.
    print(result.strip(), end="\n")
