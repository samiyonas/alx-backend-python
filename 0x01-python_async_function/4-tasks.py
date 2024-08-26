#!/usr/bin/env python3
""" execute multiple coroutines at the same time """
from typing import List
import asyncio
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ executes multiple coroutines at the same time """
    tasks = []
    result = []

    for _ in range(n):
        tasks.append(asyncio.create_task(task_wait_random(max_delay)))
    for i in asyncio.as_completed(tasks):
        task = await i
        result.append(task)
    return result
