#!/usr/bin/env python3
'''Task 2's module.
This module contains a function to measure the average execution time 
of the asynchronous function wait_n, which runs n asynchronous tasks.
'''

import asyncio
import time

# Import the wait_n function from Task 1
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measures the average time taken to execute wait_n n times.

    Args:
        n (int): The number of asynchronous tasks to run.
        max_delay (int): The maximum number of seconds each task can delay.

    Returns:
        float: The average execution time per task.
    '''
    # Record the start time before executing wait_n
    start_time = time.time()
    
    # Run wait_n asynchronously
    asyncio.run(wait_n(n, max_delay))
    
    # Compute and return the average time per task
    return (time.time() - start_time) / 
