#!/usr/bin/python3
"""define class Square"""


class Square:

    """initializes size"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """defines area as size * size """

    def area(self):
        return self.__size ** 2
