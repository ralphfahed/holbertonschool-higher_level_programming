#!/usr/bin/python3
"""Module to return the Python object represented by a JSON string."""


import json


def from_json_string(my_str):
    """
    Returns the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)  # Convert JSON string to Python object
