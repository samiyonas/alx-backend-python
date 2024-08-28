#!/usr/bin/env python3
""" Async Generator """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ async generator yielding random number """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
