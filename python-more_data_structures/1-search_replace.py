#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)  # Add 'replace' instead of 'search'
        else:
            new_list.append(item)  # Keep the original value
    return new_list
