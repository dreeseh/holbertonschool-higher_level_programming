#!/usr/bin/python3
"""
this module defines a class called Rectangle
it defines Rectangle using the file previous
class Rectangle:
"""


class Rectangle:
    """
    defined by:
    class Rectangle width
    class Rectangle height
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__height == 0 or self.__width == 0):
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return
        hash_tag = ""
        for i in range(self.height):
            for j in range(self.width):
                hash_tag += "#"
            hash_tag += "\n"
        hash_tag = hash_tag[:-1]
        return hash_tag

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
