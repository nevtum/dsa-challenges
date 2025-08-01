import pytest

from .algo import max_profit


@pytest.mark.parametrize(
    "prices,fee,expected",
    [
        ([1, 3, 2, 8, 4, 9], 2, 8),
        ([1, 3, 7, 5, 10, 3], 3, 6),
        ([4, 5, 2, 4, 3, 3, 1, 2, 5, 4], 1, 4),
    ],
)
def test_max_profit_buy_and_sell_stock(prices, fee, expected):
    assert max_profit(prices, fee) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
