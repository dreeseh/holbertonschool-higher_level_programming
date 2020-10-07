#!/usr/bin/python3
"""
module for function number_of_lines
"""


def number_of_lines(filename=""):
    """a function that returns the number of lines of a text file"""
    with open(filename, 'r') as f:
        lines = 0
        for line in f:
            lines += 1
        return lines
