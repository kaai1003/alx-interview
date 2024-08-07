#!/usr/bin/python3
"""min operations module"""


def minOperations(n: int) -> int:
    """min operations calculation function"""
    if n <= 1:
        return 0
    if n == 2:
        return 2
    copy_all = 0
    past = 0
    chars = 1
    while chars < n:
        if (n % chars) == 0:
            copy_all += 1
            past += 1
            copied = chars
            chars = chars * 2
        else:
            past += 1
            chars += copied
    if chars == n:
        return (copy_all + past)
    return 0
