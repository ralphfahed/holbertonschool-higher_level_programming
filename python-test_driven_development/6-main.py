#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))  # Expected output: 4
print(max_integer([1, 3, 4, 2]))  # Expected output: 4
print(max_integer([-1, -5, -3]))  # Expected output: -1
print(max_integer([7]))           # Expected output: 7
print(max_integer([]))            # Expected output: None
