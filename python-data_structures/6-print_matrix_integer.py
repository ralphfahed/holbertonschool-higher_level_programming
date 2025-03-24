#!/usr/bin/python3

# marix ya3ne bet2asema 3 elements w 3 rows chi hek
def print_matrix_integer(matrix=[[]]):
    for row in matrix:  # loop bi 2aleb kel row
        for element in row:  # loop bel elemetns li bel row
            print("{}".format(element), end=" ")  # Print the element with a space
        print()  # Print a new line after each row
