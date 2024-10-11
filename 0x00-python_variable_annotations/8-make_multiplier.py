#!/usr/bin/env python3
'''This module provides a function to create a multiplier function.
'''
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates and returns a function that multiplies a given float by the specified multiplier.

    Args:
        multiplier (float): The number to multiply other numbers by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns the result of multiplying it by the multiplier.
    '''
    return lambda x: x * multiplier
