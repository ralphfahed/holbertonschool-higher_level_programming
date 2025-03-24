#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:  # Loop through each row
        if row:  # If the row is not empty
            for i in range(len(row)):  # Loop through the elements by index
                if i != len(row) - 1:  # If it's not the last element
                    print("{:d}".format(row[i]), end=" ")  # Print element with space
                else:
                    print("{:d}".format(row[i]))  # Print last element without space
        else:
            print()  # Print a blank line for empty rows
