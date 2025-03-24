#!/usr/bin/python3

def delete_at(my_list=None, idx=0):
    if my_list is None:
        my_list = []

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        # Create a new list without the element at the specified index using slicing
        my_list = my_list[:idx] + my_list[idx+1:]
        return my_list
