from typing import List

# def max_profit_brute_force(prices: List[int], fee: int) -> int:
#     n = len(prices)

#     best_return = 0
#     # buy
#     for i in range(n):
#         # sell and take profit
#         for j in range(i+1, n):
#             profit1 = prices[j] - prices[i] - fee
#             # buy
#             for ii in range(j+1, n):
#                 # sell and take profit
#                 for jj in range(ii+1, n):
#                     profit2 = prices[jj] - prices[ii] - fee
#                     best_return = max(best_return, profit1 + profit2)

#     return best_return

def max_profit(prices: List[int], fee: int) -> int:
    n = len(prices)

    def best_entry(index) -> int:
        if index >= n:
            return 0

        buy = prices[index]
        # print(f"buying prices[{index}] = {buy}")

        best_return = 0
        for i in range(index+1, n):
            best_return = max(best_return, exit(i) - buy - fee)
        return best_return

    def exit(index) -> int:
        # print(f"selling prices[{index}] = {prices[index]}")
        if index >= n:
            return 0

        # return current price + any additional entry after
        return prices[index] + best_entry(index+1)

    return best_entry(0)
