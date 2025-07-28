import pytest
from .algo import jump


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0], 0),
        ([1, 2], 1),
        ([1, 1, 1], 2),
        ([2, 3, 1, 1, 4], 2),
        ([2, 0, 0], 1),
    ],
)
def test_jump(nums, expected):
    assert jump(nums) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
