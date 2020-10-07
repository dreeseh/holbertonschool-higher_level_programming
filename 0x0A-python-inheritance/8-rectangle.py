#!/usr/bin/python3
"""
module of BaseGeometry()
"""

class BaseGeometry():
    """
    a class BaseGeometry
    (based on 6-base_geometry.py)
    """

    def area(self):
        """ raises exception area is not implemented """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ class Rectangle inherited from BaseGeometry """

    def __init__(self, width, height):
        """ initializes Rectangle class """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
