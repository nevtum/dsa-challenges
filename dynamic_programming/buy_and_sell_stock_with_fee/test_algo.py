import pytest
from .algo import max_profit

@pytest.mark.parametrize("prices,fee,expected", [
    ([1,3,2,8,4,9], 2, 8),
])
def test_max_profit_buy_and_sell_stock(prices, fee, expected):
    assert max_profit(prices, fee) == expected
