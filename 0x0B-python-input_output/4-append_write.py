#!/usr/bin/python3
"""
module of append_write
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end
    of a text file (UTF8) and returns the number of characters added
    """
    with open(filename, mode='a', encoding='UTF-8') as f:
        return f.write(text)
