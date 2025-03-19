#!/usr/bin/python3

for i in range(10):            # First digit from 0 to 9
    for j in range(i + 1, 10): # Second digit must be greater than first
        if i == 8 and j == 9:  # Last combination (no comma)
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=", ")
