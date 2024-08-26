#!/usr/bin/env python3
""" The basics of async """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ delays for a random value between 0 and max_delay """
    rnd_time = random.uniform(0, max_delay)
    await asyncio.sleep(rnd_time)
    return rnd_time
