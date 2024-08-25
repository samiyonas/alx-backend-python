#!/usr/bin/env python3
""" let's duck type an iterable object """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element length function """
    return [(i, len(i)) for i in lst]
