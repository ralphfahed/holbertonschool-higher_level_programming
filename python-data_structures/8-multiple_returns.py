#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:  # Check if the string is empty
        return 0, None  # Return 0 for length and None for the first character
    else:
        length = len(sentence)
        first = sentence[0]
        return length, first

