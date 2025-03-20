#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numbers = [int(arg) for arg in sys.argv[1:]]
    total = sum(numbers)
    print(total)
