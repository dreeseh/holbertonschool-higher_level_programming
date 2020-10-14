#!/usr/bin/python3
"""
unittests for the Rectangle class
"""

import unittest
import json
import io
from contextlib import redirect_stdout
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """trying to break Rectangle"""
    @classmethod
    def setUpClass(cls):
        """adding initial values to Rectangle"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(10, 10)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(5, 6, 7, 8, 9)
        cls.r4 = Rectangle(11, 12, 13, 14)

    def test_id(self):
        """testing for functioning id"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 9)
        self.assertEqual(self.r4.id, 3)

    def test_width(self):
        """testing fo rfunctioning width"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 5)
        self.assertEqual(self.r4.width, 11)

    def test_height(self):
        """testing for functioning height"""
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r3.height, 6)
        self.assertEqual(self.r4.height, 12)

    def test_x(self):
        """testing for functioning x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r3.x, 7)
        self.assertEqual(self.r4.x, 13)

    def test_y(self):
        """testing for functioning height"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 8)
        self.assertEqual(self.r4.y, 14)

    def test_man_width(self):
        """testing that width = mandatory"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_man_height(self):
        """testing that height = mandatory"""
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_type_error_width(self):
        """tests for width's non-ints"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("reese", 4)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 4)

    def test_type_error_height(self):
        """tests for height non-ints"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(4, "reese")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(4, True)

    def test_type_error_x(self):
        """tests for x's non-ints"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(4, 4, "reese")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(4, 4, True)

    def test_type_error_y(self):
        """tests for y's non-ints"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(4, 4, 4, "reese")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(4, 4, 4, True)

    def test_value_error_width(self):
        """testing width for integers"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-4, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 4)

    def test_value_error_height(self):
        """testing height for integers"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(4, -4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(4, 0)

    def test_value_error_x(self):
        """testing x for integers"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(4, 4, -4)

    def test_value_error_y(self):
        """testing y for integers"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(4, 4, 4, -4)

    def test_area(self):
        """area test"""
        self.assertEqual(self.r1.area(), 100)
        self.assertEqual(self.r2.area(), 6)
        self.assertEqual(self.r3.area(), 30)
        self.assertEqual(self.r4.area(), 132)

    def test_too_many_area_args(self):
        """testing for too many args for area"""
        with self.assertRaises(TypeError):
            r = self.r1.area(4)

    def test_normal_diaplay(self):
        """testinf display works nornally"""
        r = Rectangle(2, 3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 10 + "\n") * 10)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n") * 3)

    def test_too_many_args_display(self):
        """testing for too many args for display"""
        with self.assertRaises(TypeError):
            self.r1.display(1)

    def test_string(self):
        """testing the string method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/10")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")
        self.assertEqual(str(self.r3), "[Rectangle] (9) 7/8 - 5/6")
        self.assertEqual(str(self.r4), "[Rectangle] (3) 13/14 - 11/12")
