#!/usr/bin/python3
"""
Module to determine the fewest number of
coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins
    needed to meet a given amount total.

    Args:
        coins (list of int): A list of the
        values of the coins in your possession.
        total (int): The total amount to make change for.

    Returns:
        int: The fewest number of coins
        needed to meet the total, or -1 if it cannot be met.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
