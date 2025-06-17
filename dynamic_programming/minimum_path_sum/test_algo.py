import pytest
from .algo import min_path_sum

@pytest.mark.parametrize("grid, expected", [
    ([[12]], 12),
    ([[1,2,3]], 6),
    ([[1,3,1],[1,5,1],[4,2,1]], 7),
])
def test_min_path_sum(grid, expected):
    assert min_path_sum(grid) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
