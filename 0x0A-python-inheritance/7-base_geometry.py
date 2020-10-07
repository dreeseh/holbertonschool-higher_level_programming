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
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
