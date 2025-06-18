import pytest

from .algo import rob


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2], 2),
        ([2, 7], 7),
        ([2, 7, 9], 11),
        ([2, 7, 9, 3], 11),
        ([2, 7, 9, 3, 1], 12),
        ([2, 7, 9, 0, 0, 0, 3, 1], 14),
    ],
)
def test_rob(nums, expected):
    assert rob(nums) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
