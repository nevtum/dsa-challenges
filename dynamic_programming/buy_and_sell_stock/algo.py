from typing import List


# Not much of a dp algorithm, but more of a greedy one
# since there is only exactly one entry and exit position
# for this problem
def max_profit(prices: List[int]) -> int:
    min_price, profit = prices[0], 0

    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        profit = max(profit, prices[i] - min_price)

    return profit
