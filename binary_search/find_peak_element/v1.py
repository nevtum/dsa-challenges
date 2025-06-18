from typing import List


def find_peak_elem(nums: List[int]) -> int:
    print(f"nums={nums}")
    n = len(nums)

    if n <= 1:
        return 0

    left, right = 0, n

    while left != right:
        mid = (right + left) // 2
        peak = nums[mid]
        print(f"peak={peak}, mid={mid}, left={left}, right={right}")

        if mid - 1 >= 0 and nums[mid - 1] > peak:
            print("bim")
            peak = nums[mid - 1]
            right = mid - 1
        elif mid + 1 <= n - 1 and nums[mid + 1] > peak:
            print("bam")
            peak = nums[mid + 1]
            left = mid + 1
        else:
            print("bom")
            return mid

    print("exited")
    assert left == right
    return left
