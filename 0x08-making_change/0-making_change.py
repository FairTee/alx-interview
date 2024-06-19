#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): A list of the values of the coins in your possession.
        total (int): The total amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total, or -1 if it cannot be met.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
