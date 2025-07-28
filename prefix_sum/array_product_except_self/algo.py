from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix_product = [0 for _ in range(n)]
    suffix_product = [0 for _ in range(n)]

    prefix, suffix = 1, 1
    for i in range(n):
        prefix *= nums[i]
        suffix *= nums[n - i - 1]
        prefix_product[i] = prefix
        suffix_product[n - i - 1] = suffix

    result = [0 for _ in range(n)]
    for i in range(n):
        before = 1 if i - 1 < 0 else prefix_product[i - 1]
        after = 1 if i + 1 >= n else suffix_product[i + 1]
        result[i] = before * after

    return result
