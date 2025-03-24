#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:  # Loop through each row
        if row:  # If the row is not empty
            for i in row:  # Loop directly over each element in the row
                print("{:d}".format(i), end=" ")  # Print element with space
            print()  # Print a new line after each row
        else:
            print()  # Print a blank line for empty rows
