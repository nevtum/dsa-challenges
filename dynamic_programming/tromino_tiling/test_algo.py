import pytest
from .algo import num_tilings


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 5),
        (6, 53),
        (8, 258),
        (9, 569),
        (30, 312342182),
    ],
)
def test_num_tilings(n, expected):
    assert num_tilings(n) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
