#!/usr/bin/python3
"""
unittests for Base class
"""

import unittest
from models import base
Base = base.Base
import json

class TestBase(unittest.TestCase):
    """contains tests for base class"""

    def test_normal_use(self):
        """tests normal use"""
        b = Base(21)
        self.assertEqual(b.id, 21)

    def test_no_id(self):
        """tests no id"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_two_args(self):
        """too many args"""
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_id_is_float(self):
        """id is a float"""
        b = Base(4.4)
        self.assertEqual(b.id, 4.4)

    def test_id_is_string(self):
        """id is a string"""
        b = Base("string")
        self.assertEqual(b.id, 'string')

    def test_id_is_neg(self):
        """id is a negative number"""
        b = Base(-44)
        self.assertEqual(b.id, -44)
    def test_nb_as_private(self):
        """nb_objects as a private instance"""
        b = Base(4)
        with self.assertRaises(AttributeError):
            print(b._nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_to_json_string(self):
        """tests json string functionality"""
        Base._Base__nb_objects = 0
        d1 = {"id": 2, "width": 3, "height": 4, "x": 5, "y": 6}
        d2 = {"id": 7, "width": 8, "height": 9, "x": 1, "y": 2}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_json_string_empty(self):
        """empty json string"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_json_string_none(self):
        """json string is None"""
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """normal from json string"""
        json_string = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
                        {"id": 2, "width": 3, "height": 4, "x": 5, "y": 6}]'
        json_l = Base.from_json_string(json_string)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5})
        self.assertEqual(json_l[1],
                         {'id': 2, 'width': 3, 'height': 4, 'x': 5, 'y': 6})

    def test_from_json_string_empty(self):
        """the string from json is empty"""
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_is_None(self):
        """the string from json is None"""
        self.assertEqual([], Base.from_json_string(None))
