#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Loop through the dictionary keys
    for existing_key in a_dictionary:
        if existing_key == key:  # if key exists
            a_dictionary[existing_key] = value  # Update oldvalue to newvalue
            break  # Exit loop once key is updated
    else:
        # If key does not exist in the dictionary, add it
        a_dictionary[key] = value
    return a_dictionary  # Return the updated dictionary
