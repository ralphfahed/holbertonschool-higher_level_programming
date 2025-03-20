#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Get the number of arguments excluding the script name
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        # If there's exactly one argument, print singular form
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        # If there are multiple arguments, print plural form
        print("{} arguments:".format(num_args))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
