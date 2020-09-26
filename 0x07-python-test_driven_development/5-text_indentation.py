#!/usr/bin/python3
"""
This module has one function that prints a text
with 2 new lines after each of these 3 chars:
. ? and :
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new
    lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    i = 0
    while i < len(text):
        print("{}".format(text[i]), end="")
        if text[i] in [".", "?", ":"]:
            print("")
            print("")
            i += 1
        i += 1
