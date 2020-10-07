#!/usr/bin/python3
"""
module of read_lines
"""


def read_lines(filename="", nb_lines=0):
    """
    a function that reads n lines of
    a text file (UTF8) and prints it to stdout:
    """
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for i in range(nb_lines):
            print(f.readline(), end="")
