#!/usr/bin/python3
"""make change Module
"""


def makeChange(coins, total):
    """make change function

    Args:
        coins (int): coins list
        total (int): total amount
    """
    if total <= 0:
        return 0
    sorted_list = sorted(coins, reverse=True)
    total_coins = 0
    new_total = 0
    rem = total
    for coin in sorted_list:
        if new_total == total:
            return total_coins
        total_coins += int(rem / coin)
        new_total += coin * int(rem / coin)
        rem = int(rem % coin)
    return -1
