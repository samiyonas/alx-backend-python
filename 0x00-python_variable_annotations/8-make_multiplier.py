#!/usr/bin/env python3
""" complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return a function that multiplies two floats """
    def fun(v: float) -> float:
        """ return a multiplication of two floats """
        return v * multiplier
    return fun
