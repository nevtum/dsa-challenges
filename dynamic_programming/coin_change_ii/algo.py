from typing import List
from functools import cache


def change(coins: List[int], amount: int) -> int:
    @cache
    def num_ways(i: int, target: int) -> int:
        if target < 0:
            return 0

        if target > amount or i >= len(coins):
            return 0

        if target == 0:
            return 1

        # choosing current coin, deducting from target value
        take = num_ways(i, target - coins[i])

        # skip current coin choosing the next coin
        # not deducting from target value
        skip = num_ways(i + 1, target)
        return take + skip

    return num_ways(0, amount)
