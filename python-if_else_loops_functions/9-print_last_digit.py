#!/usr/bin/python3

def print_last_digit(number):
    #abs ta testa2bel the negative numbers
    #ba3mol %10 ta jib ekher digit
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
