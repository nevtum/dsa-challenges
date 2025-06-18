from typing import List


def combs(nums: List[int], level: int, residual: int, result: List[List[int]]):
    # print(f"nums: {nums}, level: {level}, residual: {residual}, result: {result}")
    if residual < 0:
        return

    if level <= 0:
        # breakpoint()
        if residual == 0:
            result.append(nums)
        return

    min_val = nums[-1] if nums else 0

    for i in range(min_val + 1, 9 + 1):
        combs(nums + [i], level - 1, residual - i, result)


def combination_sum_iii(k: int, n: int) -> List[List[int]]:
    nums, result = [], []
    combs(nums, k, n, result)
    return result
