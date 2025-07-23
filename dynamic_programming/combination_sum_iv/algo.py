from typing import List


def combination_sum_iv(nums: List[int], target: int) -> int:
    if target == 0:
        return 1
    if target < 0:
        return 0

    return sum(combination_sum_iv(nums, target - num) for num in nums)
