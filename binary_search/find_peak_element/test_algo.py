import pytest

from .v1 import find_peak_elem


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], 5),
        ([1], 0),
        ([2, 1], 0),
    ],
)
def test_find_peak_elem(nums, expected):
    assert find_peak_elem(nums) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
