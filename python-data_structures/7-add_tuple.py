#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Check if tuple_a has at least 1 element, otherwise assign 0
    if len(tuple_a) > 0:
        a1 = tuple_a[0]
    else:
        a1 = 0

    # Check if tuple_a has at least 2 elements, otherwise assign 0
    if len(tuple_a) > 1:
        a2 = tuple_a[1]
    else:
        a2 = 0

    # Check if tuple_b has at least 1 element, otherwise assign 0
    if len(tuple_b) > 0:
        b1 = tuple_b[0]
    else:
        b1 = 0

    # Check if tuple_b has at least 2 elements, otherwise assign 0
    if len(tuple_b) > 1:
        b2 = tuple_b[1]
    else:
        b2 = 0

    # Add the elements of both tuples
    new_tuple = (a1 + b1, a2 + b2)

    # Return the resulting tuple
    return new_tuple
