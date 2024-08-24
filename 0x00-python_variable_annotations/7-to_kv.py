#!/usr/bin/env python3
""" complex types - string and int/float to tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple of string and float """
    v = float(v ** 2)
    new_tuple = (k, v)
    return new_tuple
