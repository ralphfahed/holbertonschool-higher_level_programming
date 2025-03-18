#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit of the number
Last_digit = abs(number) % 10  # Ensure positive digit

# If the number is negative, make last_digit negative
if number < 0:
    Last_digit = -Last_digit

# Print the results
if Last_digit > 5:
    print(f"Last digit of {number} is {Last_digit} and is greater than 5")
elif Last_digit == 0:
    print(f"Last digit of {number} is {Last_digit} and is 0")
elif Last_digit < 6 and Last_digit != 0:
    print(f"Last digit of {number} is {Last_digit} and is less than 6 "
          "and not 0")
