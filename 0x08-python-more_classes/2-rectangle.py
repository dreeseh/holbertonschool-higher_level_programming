#!/usr/bin/python3
"""
this module defines a class called Rectangle
it defines Rectangle using the file previous
class Rectangle:
"""


class Rectangle:
    """
    defiined by
    class Rectangle width
    class Rectangle height
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
