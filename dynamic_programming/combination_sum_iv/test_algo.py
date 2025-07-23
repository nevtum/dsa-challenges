import pytest
from .algo import combination_sum_iv


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 2, 3], 4, 7),
        ([9], 3, 0),
        ([3], 9, 1),
        # ([7, 13], 300, 3828068480),
    ],
)
def test_combination_sum_iv(nums, target, expected):
    assert combination_sum_iv(nums, target) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
