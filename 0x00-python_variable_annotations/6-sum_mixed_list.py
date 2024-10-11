#!/usr/bin/env python3
'''This module provides a function to compute the sum of a list containing both integers and floating-point numbers.
'''
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Computes the sum of a list of integers and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing both integers and floating-point numbers.

    Returns:
        float: The total sum of the numbers in the list, as a floating-point number.
    '''
    return float(sum(mxd_lst))
