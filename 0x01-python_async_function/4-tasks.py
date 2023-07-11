#!/usr/bin/env python3
""" This module implements multiple coroutines """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """returns a list of completed n tasks"""

    # creation of a list of concurrent tasks which start at the same time
    concurrent_tasks = [task_wait_random(max_delay)
                        for _ in range(n)]
    completed_tasks = []

    """Ensure that tasks are added in the complete tasks list according to
    their completition time. This means that the order will be ascending
    'first task to complete is first while the others follow in that order'
    """
    for task in asyncio.as_completed(concurrent_tasks):
        completed_tasks.append(await task)
    return completed_tasks
