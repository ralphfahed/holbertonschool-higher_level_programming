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

    i = 0
    while i < len(text):
        # Print current character
        print(text[i], end="")

        # If character is ., ? or :, print two newlines
        if text[i] in ".?:":
            print("\n\n", end="")
            # Skip spaces after special characters
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
