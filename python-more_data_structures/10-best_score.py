#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:  # Check if the dictionary is empty
        return None
    # Find the key with the maximum value
    # max(iterable, key=None, default=None)
    # get method to compare the values of keys
    return max(a_dictionary, key=a_dictionary.get)
