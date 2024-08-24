#!/usr/bin/env python3
""" Complex types - list of floats """


def sum_list(input_list: list[float]) -> float:
    """ returns sum of floats """
    x: float = 0
    for i in input_list:
        x += i

    return x
