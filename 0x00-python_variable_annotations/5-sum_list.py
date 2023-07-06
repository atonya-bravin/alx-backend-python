#!/usr/bin/env python3
"""
    This Module contains a function
    that takes in a list of floats and returns their sum
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
        This function takes in a list of floats and gives back the sum

        Args:
            input_list: the list of float numbers

        Return:
            The sum of all the float numbers

        Raises:
            No error checks

    """

    sum: float = 0.0

    for input in input_list:
        sum = sum + input

    return (sum)
