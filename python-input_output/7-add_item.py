#!/usr/bin/python3
"""Script that adds all arguments to a list and saves them to a JSON file."""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def main():
    """Main function that adds arguments to a list and saves to a JSON file"""
    # Get all arguments passed (excluding the script name itself)
    arguments = sys.argv[1:]

    try:
        # Try to load the existing list from the JSON file
        current_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        # If file doesn't exist, start with an empty list
        current_list = []

    # Add the new arguments to the list
    current_list.extend(arguments)

    # Save the updated list back to the JSON file
    save_to_json_file(current_list, "add_item.json")

if __name__ == "__main__":
    main()
