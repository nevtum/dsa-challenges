from typing import List

def find_peak_elem(nums: List[int]) -> int:
    print(f"nums={nums}")
    n = len(nums)

    if n <= 1:
        return 0

    l, r = 0, n

    while l != r:
        mid = (r + l) // 2
        peak = nums[mid]
        print(f"peak={peak}, mid={mid}, left={l}, right={r}")

        if mid-1 >= 0 and nums[mid-1] > peak:
            print("bim")
            peak = nums[mid-1]
            r = mid-1
        elif mid+1 <= n-1 and nums[mid+1] > peak:
            print("bam")
            peak =nums[mid+1]
            l = mid+1
        else:
            print("bom")
            return mid

    print("exited")
    assert l == r
    return l
