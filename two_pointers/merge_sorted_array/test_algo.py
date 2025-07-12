import pytest
from .algo import merge


@pytest.mark.parametrize(
    "nums1, n, nums2, m, expected",
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ],
)
def test_merge_sorted_array(nums1, n, nums2, m, expected):
    merge(nums1, n, nums2, m)
    assert nums1 == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
