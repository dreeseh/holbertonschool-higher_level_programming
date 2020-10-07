#!/usr/bin/python3
"""
module of BaseGeometry()
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inherited from BaseGeometry """

    def __init__(self, width, height):
        """ initializes Rectangle class """

        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
