from .algo import combination_sum_iii
import pytest

@pytest.mark.parametrize("k,n,expected", [
    (3, 7, [[1,2,4]]),
    (3, 9, [[1,2,6],[1,3,5],[2,3,4]]),
    (4, 1, []),
])
def test_combination_sum_iii(k, n, expected):
    assert combination_sum_iii(k, n) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
