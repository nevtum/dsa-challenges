from typing import List
from bisect import insort_left


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    assert len(nums1) == m + n

    # nothing to merge from nums2
    if n == 0:
        return

    i1, i2 = 0, 0

    while i1 < len(nums1):
        print(i1, i2)
        if nums1[i1] == 0:
            nums1[i1] = nums2[i2]
            i2 += 1
        # find index of nums2 to replace with nums1
        # at position i1 while replacing nums1 at
        # position i1 with the 0th index of nums2
        elif nums1[i1] > nums2[0]:
            # keep nums2 list in order, O(log n)
            insort_left(nums2, nums1[i1])
            nums1[i1] = nums2.pop(0)
        else:
            pass
        i1 += 1
