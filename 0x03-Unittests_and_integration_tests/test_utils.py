#!/usr/bin/env python3
"""Module for testing the utils functions.
"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests for the `access_nested_map` function."""
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),                         # Simple case: single level access
        ({"a": {"b": 2}}, ("a",), {"b": 2}),         # Nested dictionary: access first level
        ({"a": {"b": 2}}, ("a", "b"), 2),            # Nested dictionary: access second level
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests the output of `access_nested_map` against expected results."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),                       # Empty map: should raise KeyError
        ({"a": 1}, ("a", "b"), KeyError),            # Key not found in nested structure
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests that `access_nested_map` raises exceptions as expected."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests for the `get_json` function."""
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),   # Valid URL with expected payload
        ("http://holberton.io", {"payload": False}), # Another valid URL with different payload
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests the output of `get_json` against expected payload."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for the `memoize` decorator function."""
    
    def test_memoize(self) -> None:
        """Tests that `memoize` caches the output correctly."""
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
            self.assertEqual(test_class.a_property(), 42) # First call, should return 42
            self.assertEqual(test_class.a_property(), 42) # Second call, should use cached result
            memo_fxn.assert_called_once()                   # Ensure a_method was called only once
