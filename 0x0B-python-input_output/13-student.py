#!/usr/bin/python3
"""
module for class student
"""


class Student:
    """
    a class called Student
    """

    def __init__(self, first_name, last_name, age):
        """initializes Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        reeses_dict = {}
        if attrs is not None:
            for i in attrs:
                if i in self.__dict__:
                    reeses_dict[i] = self.__dict__[i]
            return reeses_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """method that replaces all attributes if the Student instance"""
        for i in self.__dict__:
            if i in json:
                self.__dict__[i] = json[i]
