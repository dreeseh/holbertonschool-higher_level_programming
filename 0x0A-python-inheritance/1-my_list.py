#!/usr/bin/python3
"""
a module for My_list
"""


class MyList(list):
    """
    class MyList
    """

    def print_sorted(self):
        """
        sorts & prints list
        """
        print(sorted(self))
