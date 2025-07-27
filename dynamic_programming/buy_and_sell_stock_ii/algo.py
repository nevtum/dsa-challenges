from typing import List


# this solution is not necessarily a dp algo, but a greedy one
# since the optimal solution will always be selling higher than
# the entry position.
def max_profit(prices: List[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        # while price movement is going up
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit
