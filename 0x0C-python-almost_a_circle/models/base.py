#!/usr/bin/python3
"""
a module of class base
"""
import json
import csv

class Base:
    """defines class as Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initializes class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        l_obj = []
        if list_objs is not None:
            for i in list_objs:
                l_obj.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(l_obj))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        loi = []
        try:
            with open(filename, 'r') as f:
                loi = cls.from_json_string(f.read())
            for i, a in enumerate(loi):
                loi[i] = cls.create(**loi[i])
        except:
            pass
        return loi

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csv_file:
            write_csv = csv.writer(csv_file)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    write_csv.writerow([obj.id,
                                        obj.width,
                                        obj.height,
                                        obj.x,
                                        obj.y])

            elif cls.__name__ is "Square":
                for obj in list_objs:
                    write_csv.writerow([obj.id,
                                        obj.size,
                                        obj.x,
                                        obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        my_list = []
        try:
            with open(filenane, 'r') as csv_file:
                read_csv = csv.reader(csv_file)
                for args in read_csv:
                    if cls.__name__ is "Rectangle":
                        csv_dict = {"id": int(args[0]),
                                    "width": int(args[1]),
                                    "height": int(args[2]),
                                    "x": int(args[3]),
                                    "y": int(args[4])}

                    elif cls.__name__ is "Square":
                        csv_dict = {"id": int(args[0]),
                                    "size": int(args[1]),
                                    "x": int(args[2]),
                                    "y": int(args[3])}
                    csv_object = cls.create(**csv_dict)

                    my_list.append(csv_object)
        except:
            pass
        return my_list
