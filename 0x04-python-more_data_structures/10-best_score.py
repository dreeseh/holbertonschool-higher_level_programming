#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest = 0
    key = None
    for l, m in a_dictionary.items():
        if m > highest:
            highest = m
            key = l
    return key
