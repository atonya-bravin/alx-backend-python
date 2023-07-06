#!/usr/bin/env python3
"""
    Takes a string k and an int OR float, returns a tuple
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        This function takes a string and int/float and returns a tuple

        Args:
            k: the string
            v: the list of mixed numbers

        Returns:
            A turple containing k and the szuare of int/float of v

        Raises:
            No error checks
    """
    return (k, v ** 2)
