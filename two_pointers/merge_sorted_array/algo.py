from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    assert len(nums1) == m + n

    mm, nn = m - 1, n - 1
    last = m + n - 1
    while mm >= 0 and nn >= 0:
        if nums1[mm] >= nums2[nn]:
            nums1[last] = nums1[mm]
            mm -= 1
        else:
            nums1[last] = nums2[nn]
            nn -= 1
        last -= 1

    while nn >= 0:
        nums1[last] = nums2[nn]
        nn -= 1
        last -= 1
