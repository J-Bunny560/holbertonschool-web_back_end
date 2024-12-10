#!/usr/bin/env python3
"""Helper function for pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """Calculates start and end indices for pagination

    Args:
        page (int): page number
        page_size (int): page size
    Returns:
    tuple: start and end indices
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
