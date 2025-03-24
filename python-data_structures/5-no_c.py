#!/usr/bin/python3
# Ma sta3malna .remove la2no hone a string
def no_c(my_string):
    new_string = ""  # create a new empty string
    for i in my_string:  # loop in the string
        if i != 'c' and i != 'C':
            new_string += i  # Add the character to the new string if it's not 'c' or 'C'
    return new_string  # Return the new string after the loop
