#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value), end='')
    except (ValueError, TypeEror):
        print("{} is not an integer".format(value))
