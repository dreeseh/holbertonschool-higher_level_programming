#!/usr/bin/python3
"""
module of write_file
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file
    (UTF8) and returns the number of characters written:
    """
    with open(filename, 'w') as f:
        return f.write(text)
