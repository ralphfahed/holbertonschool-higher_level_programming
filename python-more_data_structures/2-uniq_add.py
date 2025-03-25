#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_values = []  # New list to track unique values
    result = 0  # To store the sum
    for i in my_list:
        if i not in unique_values:  # If i is not already in the newlist
            unique_values.append(i)  # Add 'i' to the newlist
            result += i  # Add 'i' to the total sum
    return result
