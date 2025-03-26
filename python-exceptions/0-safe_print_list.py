#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0  # Initialize the count variable
    try:
        for i in range(x):
            print(my_list[i])
            count += 1  # Increment the count for each printed element
    except:
        pass  # If the index exceeds the list length, just ignore the error
    print()  # Print a newline at the end
    return count  # Return the number of printed elements
