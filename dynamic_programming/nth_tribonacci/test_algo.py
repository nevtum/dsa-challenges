from .algo import tribonacci
import pytest

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (4, 4),
    (5, 7),
    (25, 1389537),
])
def test_tribonacci(n, expected):
    assert tribonacci(n) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
