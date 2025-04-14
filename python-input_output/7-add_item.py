#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file"""
import sys
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = "add_item.json"

# Initialize or load the list
if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add all arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list
save_to_json_file(my_list, filename)
