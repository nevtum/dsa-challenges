import pytest
from .algo import productExceptSelf


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        # ([], []),
        # ([], []),
    ],
)
def test_product_except_self(nums, expected):
    assert productExceptSelf(nums) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
