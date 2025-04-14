"""Module to read and print a UTF-8 text file to stdout."""

#!/usr/bin/python3


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
