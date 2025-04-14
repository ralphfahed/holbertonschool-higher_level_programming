#!/usr/bin/python3
"""Module that defines a function to write a object to a fil in JSON format"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation."""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
