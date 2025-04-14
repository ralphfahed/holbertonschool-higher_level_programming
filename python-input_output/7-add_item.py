#!/usr/bin/python3
"""Script that adds command line args to a Python list and saves to a JSON file"""
import sys

# Import functions from other scripts
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
