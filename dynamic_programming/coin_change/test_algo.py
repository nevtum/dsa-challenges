import pytest

from .algo import coin_change_memoization, coin_change_tabulation


@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        ([], 0, 0),
        ([1], 0, 0),
        ([1], 1, 1),
        ([2, 5, 10], 1, -1),
        ([1, 3, 4], 6, 2),
        ([5], 10, 2),
        ([2, 5, 10, 20, 50], 100, 2),
    ],
)
def test_coin_change(coins, amount, expected):
    assert coin_change_memoization(coins, amount) == expected
    assert coin_change_tabulation(coins, amount) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
