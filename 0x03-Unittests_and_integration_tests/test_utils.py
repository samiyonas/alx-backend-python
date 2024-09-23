#!/usr/bin/env python3
""" unit test """
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ This class is used to test 'access_nested_map' function from utils """
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

    @parameterized.expand(
            [
                ({}, ("a",), KeyError),
                ({"a": 1}, ("a", "b"), KeyError)
                ]
            )
    def test_access_nested_map_exception(self, nested_map, path, result):
        """ tests that KeyError is raised for the above inputs """
        with self.assertRaises(result):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ This class is used to test 'get_json' function from utils """
    @parameterized.expand(
            [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False})
                ]
            )
    def test_get_json(self, test_url, test_payload):
        """ tests get_json function by mocking the HTTP call """
        with patch("utils.requests.get") as mocked:
            mocked.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mocked.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Tests the 'memoize' function """
    def test_memoize(self):
        """ Tests memoize's output """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
