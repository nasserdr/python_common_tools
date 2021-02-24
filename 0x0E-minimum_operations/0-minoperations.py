#!/usr/bin/python3
"""
Minimum operations file
"""


def minOperations(n):
    """
    Finds the minimum number of minOperations
    """
    res = 0
    for i in range(2, n+1):
        while n % i == 0:
            res += i
            n = n/i
    return res
