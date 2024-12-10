#!/usr/bin/env python3
"""This file contains the Async_comprehension function"""


import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns a list of floats using async comprehension"""
    return [num async for num in async_generator()]
