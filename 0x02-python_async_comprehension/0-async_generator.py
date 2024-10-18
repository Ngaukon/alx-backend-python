#!/usr/bin/env python3
'''Task 0's modules.
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Generates a sequence of ten numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
