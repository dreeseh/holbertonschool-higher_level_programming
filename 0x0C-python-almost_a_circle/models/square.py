#!/usr/bin/python3
"""module of square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class named Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """updates attributes"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                if i == 1:
                    self.size = a
                if i == 2:
                    self.x = a
                if i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        di = {}
        di["id"] = self.id
        di["size"] = self.size
        di["x"] = self.x
        di["y"] = self.y
        return di
