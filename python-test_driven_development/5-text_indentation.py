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

    # Remove spaces at the beginning and end of each line
    text = text.strip()

    # Replace special characters with themselves + two newlines
    for char in ".?:":
        text = text.replace(char, char + "\n\n")

    # Split text into lines and process each line
    lines = text.split("\n")
    formatted_lines = []
    for line in lines:
        # Remove trailing and leading spaces for each line
        line = line.strip()
        if line:  # Only add non-empty lines
            formatted_lines.append(line)

    # Join lines with newline and print
    print("\n".join(formatted_lines), end="")
