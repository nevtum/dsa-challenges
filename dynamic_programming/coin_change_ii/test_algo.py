import pytest

from .algo import change


@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        ([1, 2, 5], 0, 1),
        ([1, 2, 5], 1, 1),
        ([10], 10, 1),
        ([1, 2, 5], 2, 2),
        ([1, 2, 5], 5, 4),
        ([3], 2, 0),
    ],
)
def test_coin_change(coins, amount, expected):
    assert change(coins, amount) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
