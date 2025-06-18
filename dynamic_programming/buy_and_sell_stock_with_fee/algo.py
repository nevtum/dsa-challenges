from typing import Dict, List, Tuple


def max_profit(prices: List[int], fee: int) -> int:
    n = len(prices)
    # Memoization cache to store computed results
    # State is defined by (index, is_holding_stock)
    memo: Dict[Tuple[int, bool], int] = {}

    def dp(index: int, holding: bool) -> int:
        # Base case: if we've reached the end of prices
        if index == n:
            return 0

        # Check if result is already memoized
        if (index, holding) in memo:
            return memo[(index, holding)]

        # If not holding a stock, we have two choices:
        # 1. Buy a stock
        # 2. Do nothing
        if not holding:
            # amount spent + maximum profit from next possible transactions while holding
            buy = -prices[index] + dp(index + 1, True)
            wait = dp(index + 1, False)
            result = max(wait, buy)

        # If holding a stock, we have two choices:
        # 1. Sell the stock
        # 2. Ride it out
        else:
            # Sell the stock: amount profited (less the fee) + maximum
            # profit from next possible transactions while not yet entered
            sell = prices[index] - fee + dp(index + 1, False)
            ride_it = dp(index + 1, True)

            result = max(sell, ride_it)

        # Memoize and return the result
        memo[(index, holding)] = result
        return result

    # Start with no stock at index 0
    return dp(0, False)
