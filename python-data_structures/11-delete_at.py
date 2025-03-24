#!/usr/bin/python3

def delete_at(my_list=None, idx=0):
    # Initialize my_list to an empty list if it is None
    if my_list is None:
        my_list = []
    
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list[:idx] + my_list[idx+1:]
    return new_list
