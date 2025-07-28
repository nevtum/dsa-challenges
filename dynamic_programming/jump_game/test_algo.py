import pytest
from .algo import can_jump


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([0], True),
        ([1, 2], True),
        ([1, 1, 1], True),
        ([2, 3, 1, 1, 4], True),
        ([2, 0, 0], True),
        ([0, 1], False),
        ([3, 2, 1, 0, 4], False),
        ([0, 2, 3], False),
    ],
)
def test_can_jump(prices, expected):
    assert can_jump(prices) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
