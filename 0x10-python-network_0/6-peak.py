#!/usr/bin/python3
"""
a module for:
a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    a function that finds a peak in a list of unsorted integers
    """

    my_list = list_of_integers
    if not my_list:
        return None

    if len(my_list) > 1:
        if my_list[0] >= my_list[1]:
            return my_list[0]
        if my_list[-1] >= my_list[-2]:
            return my_list[-1]
        for x in range(len(my_list)):
            if my_list[x] > my_list[x-1] and my_list[x] > my_list[x+1]:
                return my_list[x]
    return my_list[0]
