#!/usr/bin/env python3
""" The basics of async """
import random, aysncio


async def wait_random(max_delay=10):
    """ delays for a random value between 0 and max_delay """
    rnd_time = await random.uniform(0, max_delay)
    return rnd_time
