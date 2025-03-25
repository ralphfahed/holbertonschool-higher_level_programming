#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Sort the dictionary keys and print the key-value pairs
    for key in sorted(a_dictionary.keys()):  # Sorts the dictionary keys
        print(f"{key}: {a_dictionary[key]}")  # Prints each key : value
