from typing import List


def combination_sum_iv(nums: List[int], target: int) -> int:
    memo = {}

    def dfs(remaining: int) -> int:
        if remaining in memo:
            return memo[remaining]

        if remaining == 0:
            return 1
        if remaining < 0:
            return 0

        # sum all viable paths leading to target sum
        result = sum(dfs(remaining - num) for num in nums)
        memo[remaining] = result
        return result

    return dfs(target)
