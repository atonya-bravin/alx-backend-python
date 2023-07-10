#!/usr/bin/env python3
"""
This module contains a method wait_random that returns a value
passed to it in a random number of seconds between two numbers.
"""


import random
import asyncio


async def wait_random(max_delay=10):
    """
    This function returns the max_delay passed to it within a
    given random time between 0 and max_delay
    """

    delay = random.uniform(0.0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
