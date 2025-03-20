#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[1:]]  # Convert arguments to integers
    total = sum(numbers)  # Sum up the integers
    print(total)
