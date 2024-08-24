#!/usr/bin/env python3
""" Complex types - list of floats """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns sum of floats """
    x: float = 0.0
    for i in input_list:
        x += i

    return x
