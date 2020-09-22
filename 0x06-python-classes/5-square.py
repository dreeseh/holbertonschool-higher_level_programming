#!/usr/bin/python3
"""defines class of Square"""


class Square:
    """initializes size at 0"""

    def __init__(self, size=0):
        self.size = size

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

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
