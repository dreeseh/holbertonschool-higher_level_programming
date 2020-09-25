#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_normal_use(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def no_input(self):
        self.assertFalse(max_integer())

    def empty_list(self):
        self.assertFalse(max_integer([]))

    def negative_list(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def dups_in_list(self):
        self.assertEqual(max_integer([1, 2, 4, 4]), 4)

    def only_one_input(self):
        self.assertEqual(max_integer([4]), 4)

    def test_for_long_int(self):
        self.assertEqual

    @unittest.expectedFailure
    def no_int_in_list(self):
        with self.assertRaises(TypeError):
            max_integer(['i', 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
