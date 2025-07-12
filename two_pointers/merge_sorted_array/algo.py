from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    assert len(nums1) == m + n

    # nothing to merge from nums2
    if n == 0:
        return

    i1, i2 = 0, 0

    while i1 < len(nums1):
        if nums1[i1] == 0:
            nums1[i1] = nums2[i2]
            i2 += 1
        # swap out first index of nums2 with nums1 at position i1
        elif nums1[i1] > nums2[0]:
            nums1[i1], nums2[0] = nums2[0], nums1[i1]
        else:
            pass
        i1 += 1
