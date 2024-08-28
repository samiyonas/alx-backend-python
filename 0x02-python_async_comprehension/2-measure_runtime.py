#!/usr/bin/env python3
""" measure the runtime """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure the runtime """
    tasks = [async_comprehension() for _ in range(4)]
    started = time.time()

    await asyncio.gather(*tasks)

    ended = time.time()

    return ended - started
