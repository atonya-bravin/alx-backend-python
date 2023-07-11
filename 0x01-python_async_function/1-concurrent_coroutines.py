#!/usr/bin/env python3
"""This module contains the wait_n function"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    This method takes in two integers, n and max_delay,
    then spawns the wait_random function, n number of times,
    with a max_delay.
    """

    randoms = []

    for counter in range(n):
        # call the wait_random method while awaiting on it
        random_value = await wait_random(max_delay)

        #just insert the value in the list index 0 if empty
        if len(randoms) == 0:
            randoms.insert(0, random_value)

        #if value is greter than or equal to last value, append it 
        elif random_value >= randoms[len(randoms) - 1]:
            randoms.append(random_value)

        #go through the list, inserting the value in corect index in the list
        else:
            for index in range(len(randoms)):
                if random_value < randoms[index]:
                    randoms.insert(index, random_value)
                    break
    return randoms
