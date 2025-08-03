from typing import List


def combination_sum_iv_memoization(nums: List[int], target: int) -> int:
    memo = {}

    def dfs(tgt: int) -> int:
        if tgt in memo:
            return memo[tgt]

        if tgt == 0:
            return 1
        if tgt < 0:
            return 0

        # sum all viable paths leading to target sum
        result = sum(dfs(tgt - num) for num in nums)
        memo[tgt] = result
        return result

    return dfs(target)


def combination_sum_iv_tabulation(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1

    for tgt in range(1, target + 1):
        for num in nums:
            # overshot the target
            if tgt < num:
                continue

            # sum all viable paths leading to target sum
            dp[tgt] += dp[tgt - num]

    return dp[target]
