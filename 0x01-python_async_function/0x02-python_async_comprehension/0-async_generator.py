#!/usr/bin/env python3
"""
This is a module that contains a method async_generator
that loops 10 times, each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module.
"""


import asyncio
import random


async def async_generator():
    """
    loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for counter in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
