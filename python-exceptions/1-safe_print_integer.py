#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value), end='')
        return 1
    except (ValueError, TypeEror):
        return 0
