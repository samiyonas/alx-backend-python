#!/usr/bin/env python3
""" measure the runtime """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure the runtime """
    started = time.time()

    asyncio.run(wait_n(n, max_delay))

    lasted = time.time()

    return (lasted - started) / n
