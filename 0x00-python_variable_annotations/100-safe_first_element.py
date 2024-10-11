#!/usr/bin/env python3
'''This module provides a function to safely retrieve the first element of a sequence.
'''
from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Retrieves the first element of a sequence if it exists; otherwise, returns None.

    Args:
        lst (Sequence[Any]): A sequence (such as a list or tuple) from which to retrieve the first element.

    Returns:
        Union[Any, None]: The first element of the sequence if it exists, or None if the sequence is empty.
    '''
    if lst:
        return lst[0]
    else:
        return None
