#!/usr/bin/env python3
'''This module provides a function to create multiple copies of items in a tuple.
'''
from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Creates multiple copies of each item in the given tuple.

    Args:
        lst (Tuple): A tuple of items to be duplicated.
        factor (int, optional): The number of times to duplicate each item. Defaults to 2.

    Returns:
        List: A list containing the duplicated items.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in

# Example usage:
array = (12, 72, 91)

zoom_2x = zoom_array(array)  # Duplicates each item in the tuple 2 times.

zoom_3x = zoom_array(array, 3)  # Duplicates each item in the tuple 3 times.
