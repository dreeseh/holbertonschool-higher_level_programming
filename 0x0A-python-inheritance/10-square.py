#!/usr/bin/python3
"""
module of BaseGeometry()
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class of Square inhereted from Rectangle"""

    def __init__(self, size):
        """initializes Square"""

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """returns Square's area"""

        return self.__size ** 2
