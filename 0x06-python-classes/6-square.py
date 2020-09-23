#!/usr/bin/python3
""" defines Square as a class """


class Square:

    """ initializes square """

    def __init__(self, size=0, position=(0, 0)):
        if type(position) is not tuple or len(position) is not 2\
         or type(position[0]) is not int or type(position[1]) is not int\
         or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(position) is not tuple or len(position) is not 2\
         or type(position[0]) is not int or type(position[1]) is not int\
         or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for lines in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for spaces in range(self.__position[0]):
                    print(' ', end='')
                for hashes in range(self.__size):
                    print('#', end='')
                print()
