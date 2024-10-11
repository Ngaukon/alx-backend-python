#!/usr/bin/env python3
'''This module provides a function to create a tuple containing a key and the square of its value.
'''
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple, where the key is a string
    and the value is the square of the given number (int or float).

    Args:
        k (str): The key, represented as a string.
        v (Union[int, float]): The value, which can be an integer or a floating-point number.

    Returns:
        Tuple[str, float]: A tuple containing the key as a string and the square of the value as a float.
    '''
    return (k, float(v**2))
