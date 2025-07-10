import pytest
from .algo import total_cost

@pytest.mark.parametrize("costs, k, candidates, expected", [
    ([3,2,7,7,1,2], 2, 2, 3),
    ([17,12,10,2,7,2,11,20,8], 3, 4, 11),
    ([1,2,4,1], 3, 3, 4),
    ([69,10,63,24,1,71,55,46,4,61,78,21,85,52,83,77,42,21,73,2,80,99,98,89,55,94,63,50,43,62,14], 21, 31, 829),
    ([57,33,26,76,14,67,24,90,72,37,30], 11, 2, 526),
])
def test_total_cost(costs, k, candidates, expected):
    assert total_cost(costs, k, candidates) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
