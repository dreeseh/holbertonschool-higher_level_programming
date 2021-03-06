#!/usr/bin/python3
"""
module of pascal_triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """
    if n <= 0:
        return ""

    start = [[1]]
    for next_row in range(1, n):
        row = [1]
        prev_row = start[next_row - 1]
        for elem in range(1, next_row):
            row.append(prev_row[elem] + prev_row[elem - 1])
        row.append(1)
        start.append(row)
    return start
