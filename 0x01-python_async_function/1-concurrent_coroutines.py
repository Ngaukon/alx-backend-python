#!/usr/bin/env python3
'''Task 1's module.
This module contains an asynchronous coroutine that executes another
coroutine multiple times and returns the results in a sorted order.
'''

import asyncio
from typing import List

# Import the wait_random function from Task 0
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes the wait_random function n times, waits asynchronously, 
    and returns the list of wait times sorted in ascending order.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum number of seconds to delay for each call.

    Returns:
        List[float]: A sorted list of wait times from the wait_random calls.
    '''
    # Use asyncio.gather to execute all wait_random coroutines concurrently
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    # Return the sorted list of wait times
    return sorted(wait_times)
