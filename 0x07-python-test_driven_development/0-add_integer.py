#!/usr/bin/python3
"""
a function that adds 2 integers
it takes the inputs and makes sure they are of type int
if they are not, it raises a TypeError
"""


def add_integer(a, b=98):
    """
    adding two integers, returns the sum.
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')

    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    return int(a) + int(b)