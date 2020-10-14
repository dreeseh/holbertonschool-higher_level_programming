#!/Usr/bin/python3
"""
Unittest for the square class
"""

import unittest
import json
from models import square
from models.base import Base
Square = square.Square


class TestSquare(unittest.TestCase):
    """tests the square class"""
    def setUp(cls):
        """sets up the tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)
        cls.s3 = Square(4, 5, 6)
        cls.s4 = Square(7, 8, 9, 10)

    def test_id(self):
        """tests the id"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 10)

    def test_size(self):
        """tests size"""
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 4)
        self.assertEqual(self.s4.size, 7)

    def test_height(self):
        """tests height"""
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 4)
        self.assertEqual(self.s4.height, 7)

    def test_x(self):
        """tests x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)
        self.assertEqual(self.s4.x, 8)

    def test_y(self):
        """tests y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_mand_size(self):
        """tests width is mandatory"""
        with self.assertRaises(TypeError):
            s = Square()

    def test_type_error_size(self):
        """tests non-integers for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("reese")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(True)

    def test_type_error_x(self):
        """tests non-integers for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(4, "reese")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(4, True)

    def test_type_error_y(self):
        """tests non-integers for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(4, 4, "reese")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(4, 4, True)
