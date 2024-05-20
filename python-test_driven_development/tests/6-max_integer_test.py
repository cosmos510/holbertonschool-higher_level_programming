#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""
    def test_ordere_list(self):
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)

    def test_max_begiining(self):
        list = [4, 2, 3, 1]
        self.assertEqual(max_integer(list), 4)

    def test_max_middle(self):
        list = [1, 5, 3, 2]
        self.assertEqual(max_integer(list), 5)

    def test_negativ_num(self):
        list = [1, -2, 3, 4]
        self.assertEqual(max_integer(list), 4)

    def test_only_negativ_num(self):
        list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list), -1)
    
    def test_one_el_in_list(self):
        list = [4]
        self.assertEqual(max_integer(list), 4)

    def test_negativ_num(self):
        list = []
        self.assertEqual(max_integer(list), None)

    