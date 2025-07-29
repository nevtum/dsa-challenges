import pytest

from .algo import count_bits


@pytest.mark.parametrize(
    "n, expected",
    [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
    ],
)
def test_count_bits(n, expected):
    assert count_bits(n) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
