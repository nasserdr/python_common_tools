#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    Print the PT
    """
    if n <= 0:
        return []
    else:
        list = [[] for i in range(0,n)]
        for i in range(1, n):
            part = [x+1 for x in range(1,i+1)]
        list[i] = part
    return list