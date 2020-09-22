#!/usr/bin/python3
"""defines class Square"""


class Square:

    """initializes size"""

    def __init__(self, size=0):
        self.size = size

    """defines area"""

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
