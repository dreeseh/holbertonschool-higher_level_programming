#!/usr/bin/python3
"""
contains defdef text_indentation(text): which:
is a a function that prints a text with 2 new
lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """

    characters = ['.', '?', ':']

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    text_new = text.strip()

    for i, v in enumerate(text_new):
            if v in characters:
                print("{:s}\n".format(v))
            else:
                if (text_new[i - 1] in characters \
                or (text_new[i] == ' ' \
                and text_new[i - 1] == ' ')):
                    continue
                print("{:s}".format(v), end="")
    print()
