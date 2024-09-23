#!/usr/bin/env python3
""" Parametrize a unit test """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ This class used to test 'access_nested_map' function from utils """
    @parameterized.expand(
            [
                ({"a": 1}, ("a",), 1),
                ({"a": {"b": 2}}, ("a",), {"b": 2}),
                ({"a": {"b": 2}}, ("a", "b"), 2)
                ]
            )
    def test_access_nested_map(self, nested_map, path, result):
        """ This method tests access_nested_map function """
        self.assertEqual(access_nested_map(nested_map, path), result)
