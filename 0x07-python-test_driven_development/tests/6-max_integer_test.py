#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_last(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_first(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_middle(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_one_negative(self):
        self.assertEqual(max_integer([1, -2, 3, 4]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
 
