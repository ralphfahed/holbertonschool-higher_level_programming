#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:  # Catch the case when x is larger than the list length
            break  # Stop the loop once we reach an invalid index
    print()  # Print a new line after printing integers
    return count
