#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:  # Loop through each row
        for i, element in enumerate(row):  # Use enumerate to track the index
            if i != len(row) - 1:  # If it's not the last element in the row
                print("{:d}".format(element), end=" ")  # Print element with space
            else:
                print("{:d}".format(element))  # Print last element without space
