import pytest
from .algo import min_path_sum

@pytest.mark.parametrize("grid, expected", [
    ([[12]], 12),
    ([[1,2,3], 6]),
])
def test_min_path_sum(grid, expected):
    assert min_path_sum(grid) == expected
