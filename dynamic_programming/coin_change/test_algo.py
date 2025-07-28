import pytest
from .algo import coin_change


@pytest.mark.parametrize(
    "coins, amount, expected",
    [
        ([], 0, 1),
        ([1], 0, 1),
        ([1, 3, 4], 6, 2),
    ],
)
def test_coin_change(coins, amount, expected):
    assert coin_change(coins, amount) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
