#!/usr/bin/env python3
""" duck typing - first element of a sequence """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ safe first function """
    if lst:
        return lst[0]
    else:
        return None
