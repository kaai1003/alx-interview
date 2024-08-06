#!/usr/bin/python3
"""min operations module"""


def minOperations(n: int) -> int:
    """min operations calculation function"""
    if n <= 1:
        return 0
    if n == 2:
        return 2
    copy_all = 1
    past = 0
    fctr = 2
    while fctr <= n:
        if (n % fctr) == 0 and fctr < n:
            if (n % (fctr + 1)) == 0:
                past += 1
                fctr += 1
                continue
            copy_all += 1
            for _ in range(int(n / fctr)):
                past += 1
            return (copy_all + past)
        past += 1
        fctr += 1
    return (copy_all + past)
