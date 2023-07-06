#!/usr/bin/env python3
"""
    This module contains a method sum_mixed_list
    that takes in a list of integers and floats, then gives the sum
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
        This function takes in a list of mixed integers and floats
        then gives back their equivalent sum

        Args:
            mxd_lst: the list of mixed integers and floats

        Return:
            Returns the sum of the number in the list as float

        Raises:
            No error checks

    """

    sum: float = 0.0

    for item in mxd_lst:
        sum = sum + item

    return (sum)
