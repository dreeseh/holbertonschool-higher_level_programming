#!/usr/bin/python3
"""
a function that prints a square with the character #
"""
def print_square(size):
    """
    raises approprate errors TypeErrors
    and prints a square using #
    no return
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    if not isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    if isinstance(size, int) and size > 0:
        for i in range(size):
            for j in range(size - 1):
                print('#', end='')
            print('#')
