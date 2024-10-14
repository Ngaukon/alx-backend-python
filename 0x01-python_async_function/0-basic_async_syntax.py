#!/usr/bin/env python3
'''Task 0's module.
This module contains an asynchronous coroutine that waits for a random
number of seconds before returning the actual wait time.
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Asynchronously waits for a random amount of time between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum number of seconds to wait. Defaults to 10.

    Returns:
        float: The actual number of seconds waited (randomly generated).
    '''
    # Generate a random wait time between 0 and max_delay
    wait_time = random.random() * max_delay
    # Asynchronously sleep for the generated wait time
    await asyncio.sleep(wait_time)
    # Return the actual wait time
    return wait_time
