#!/usr/bin/env python3
'''This module provides a function to compute the lengths of sequences in an iterable.
'''
from typing import Iterable, List, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the lengths of sequences within an iterable and returns them as a list of tuples.

    Each tuple contains the sequence and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences (e.g., lists, strings, etc.).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains a sequence and its length.
    '''
    return [(i, len(i)) for i in lst]
