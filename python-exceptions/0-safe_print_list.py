#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end=' ')  # Print each element with space
    except IndexError:  # Handle case where x exceeds the list length
        pass
    print()  # Ensure there's a newline at the end
