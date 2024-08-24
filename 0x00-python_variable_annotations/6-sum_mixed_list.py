#!/usr/bin/env python3
""" Complex types - mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ returns sum of the list """
    x: float = 0
    for i in mxd_lst:
        x += i
    return x
