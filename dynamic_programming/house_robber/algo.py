from typing import List


def rob(nums: List[int]) -> int:
    n = len(nums)

    if n == 1:
        return nums[0]
    elif n == 2:
        return max(nums[:2])

    best_steal = [
        nums[0],
        max(nums[:2]),
        nums[2] + nums[0],
    ]

    for i in range(3, n):
        best = nums[i] + max(best_steal[:2])
        best_steal = best_steal[-2:] + [best]

    return max(best_steal[-2:])
