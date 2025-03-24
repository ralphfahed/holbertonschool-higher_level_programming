#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if the index is out of range (negative or greater than the list length)
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the list unchanged if index is invalid
    else:
        # Remove the element at the given index using slicing
        my_list = my_list[:idx] + my_list[idx+1:]
        return my_list
