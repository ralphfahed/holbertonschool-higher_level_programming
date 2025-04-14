"""Module that provides a function to read and print a UTF-8 text file to stdout."""

#!/usr/bin/python3
# Function that reads a UTF-8 text file and prints its contents to stdout

def read_file(filename=""):
    # Use 'with' to open the file safely and ensure it closes automatically
    with open(filename, encoding="utf-8") as f:
        # Read the entire file content and print it without adding extra newline
        print(f.read())
