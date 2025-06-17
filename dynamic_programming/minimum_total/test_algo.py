import pytest
from .algo import minimum_total

@pytest.mark.parametrize("triangle, expected", [
    ([[2]], 2),
    ([[2],[3,4]], 5),
    ([[2],[3,4],[6,5,7]], 10),
    ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
    ([[-1],[2,3],[1,-1,-3]], -1),
])
def test_minimum_total(triangle, expected):
    assert minimum_total(triangle) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
