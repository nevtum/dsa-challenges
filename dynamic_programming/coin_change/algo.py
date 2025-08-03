from functools import cache
from typing import List


def coin_change_memoization(coins: List[int], amount: int) -> int:
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


def coin_change_tabulation(coins: List[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for target in range(1, amount + 1):
        for coin in coins:
            new_target = target - coin

            # overshot the target
            if new_target < 0:
                continue

            # one extra coin plus the best min number
            # of coins from overlapping subproblem
            dp[target] = min(dp[target], 1 + dp[new_target])

    result = dp[amount]
    if result < float("inf"):
        return int(result)
    return -1
