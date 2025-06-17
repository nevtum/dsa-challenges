import pytest
from .algo import unique_paths

@pytest.mark.parametrize("n,m,expected", [
    (3, 3, 6),
    (3, 7, 28),
])
def test_unique_paths(n, m, expected):
    assert unique_paths(n, m) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
