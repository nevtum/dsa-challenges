import pytest
from .algo import min_cost_connect_points

@pytest.mark.parametrize("points, expected", [
    ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
    ([[3,12],[-2,5],[-4,1]], 18),
    ([[0,0],[1,1],[1,0],[-1,1]], 4),
])
def test_min_cost(points, expected):
    assert min_cost_connect_points(points) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
