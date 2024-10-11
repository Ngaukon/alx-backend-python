#!/usr/bin/env python3
'''This module provides a function to safely retrieve a value from a dictionary using a specified key.
'''
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Retrieves a value from a dictionary using a specified key. If the key does not exist,
    it returns a default value instead.

    Args:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key whose associated value is to be retrieved.
        default (Def, optional): The value to return if the key is not found. Defaults to None.

    Returns:
        Res: The value associated with the key if it exists, otherwise the default value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
