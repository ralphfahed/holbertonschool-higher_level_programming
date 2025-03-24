#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[:idx] + my_list[idx+1:]
    return new_list

