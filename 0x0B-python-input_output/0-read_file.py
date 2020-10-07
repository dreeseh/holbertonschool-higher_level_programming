#!/usr/bin/python3
"""module of read_file"""


def read_file(filename=""):
    """reads a text file in UTF-8 """
    with open(filename, 'r'') as f:
        print(f.read(), end="")
