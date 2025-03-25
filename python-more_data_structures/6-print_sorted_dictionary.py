#!/usr/bin/python3

def print_sorted_list_of_dictionaries(list_of_dicts):
    for a_dictionary in list_of_dicts:
        for key in sorted(a_dictionary.keys()):
            print(f"{key}: {a_dictionary[key]}")
# for a_dictionary in list_of_dicts: This loops over each dictionary in list.
# for key in sorted(a_dictionary.keys()):  we sort its keys in ascending order
# print(f"{key}: {a_dictionary[key]}"): sorted key, we print the key and value
