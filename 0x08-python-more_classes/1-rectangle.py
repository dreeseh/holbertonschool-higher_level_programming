#!/usr/bin/python3
"""
this module defines a class called Rectangle
it defines Rectangle using the file previous
"""


class Rectangle:
    """
    class Rectangle - defined by:
    private instance attribute width,
    private instance attribute height
    """

    def __init__(self, width=0, height=0):
        """ initializes rectangle """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ defines width """

        return self.__width

    @property
    def height(self):
        """defines height """

        return self.__height

    @width.setter
    def width(self, value):
        """ sets the value of width """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets the value of height """

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
