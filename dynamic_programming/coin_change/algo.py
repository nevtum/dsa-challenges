from typing import List
from functools import cache


def coin_change(coins: List[int], amount: int) -> int:
    @cache
    def dp(target: int) -> int:
        if target == 0:
            return 0

        if target < 0:
            # overshot the target
            return float("inf")

        best = float("inf")
        for coin in coins:
            new_target = target - coin
            # one extra coin plus the best min number
            # of coins from overlapping subproblem
            best = min(best, 1 + dp(new_target))

        return best

    result = dp(amount)
    if result < float("inf"):
        return result
    return -1
