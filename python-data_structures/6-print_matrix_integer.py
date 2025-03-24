#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:  # Loop through each row
        if row:  # If the row is not empty
            for i in range(len(row)):
                if i != len(row) - 1:
                    print("{:d}".format(row[i]), end=" ")
                else:
                    print("{:d}".format(row[i]))
        else:
            print()
