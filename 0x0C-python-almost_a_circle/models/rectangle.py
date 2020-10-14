#!/usr/bin/python3
"""
module of class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """defines class rectangle using base as a superclass"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes class of rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle using #"""
        print("\n" * self.__y, end='')
        for i in range(self.__height):
              print(' ' * self.__x, end='')
              print('#' * self.__width)

    def __str__(self):
        """returns the print ans string rep of a rectangle"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                            self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates the rectangle"""
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                if i == 1:
                    self.width = a
                if i == 2:
                    self.height = a
                if i == 3:
                    self.x = a
                if i == 4:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        di = {}
        di["id"] = self.id
        di["width"] = self.width
        di["height"] = self.height
        di["x"] = self.x
        di["y"] = self.y
        return di
