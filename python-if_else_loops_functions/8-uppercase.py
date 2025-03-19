#!/usr/bin/python3

def to_uppercase(str):
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result

print("Converted String: {}".format(uppercased_string))
print("Number of occurrences of '{}' is: {}".format(pattern, occurrences))
