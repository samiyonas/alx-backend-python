#!/usr/bin/env python3
""" complex types - string and int/float to tuple """
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """ returns a tuple of string and float """
    Tuple = (k, float(v**2))
    return Tuple
