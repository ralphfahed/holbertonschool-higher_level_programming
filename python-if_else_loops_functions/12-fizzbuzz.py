#!/usr/bin/python3

#print from 1 to 100 separeted by a space
#for numbers which are multiples of both three and five print FizzBuzz
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")  # First check for both 3 and 5
        elif i % 3 == 0:
            print("Fizz", end=" ")  # Then check for multiples of 3
        elif i % 5 == 0:
            print("Buzz", end=" ")  # Then check for multiples of 5
        else:
            print(i, end=" ")  # Print the number if not divisible by 3 or 5
