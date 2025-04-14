#!/usr/bin/python3
"""Module to return the JSON string representation of an object."""


import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of an object.

    Args:
        my_obj (object): The Python object to convert.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)  # Convert Python object to JSON string
