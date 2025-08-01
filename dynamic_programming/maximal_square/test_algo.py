import pytest

from .algo import maximal_square


@pytest.mark.parametrize(
    "matrix, expected",
    [
        (
            [["0", "1"], ["1", "0"]],
            1,
        ),
        ([["0"]], 0),
        (
            [
                ["0", "1", "1"],
                ["1", "1", "1"],
                ["1", "1", "1"],
            ],
            4,
        ),
        (
            [
                ["1", "1", "0"],
                ["1", "1", "1"],
                ["1", "1", "1"],
            ],
            4,
        ),
        (
            [
                ["1", "1", "1"],
                ["1", "1", "1"],
                ["0", "1", "1"],
            ],
            4,
        ),
        (
            [
                ["1", "1", "1"],
                ["1", "0", "1"],
                ["1", "1", "1"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "1"],
                ["1", "1", "1"],
                ["1", "1", "1"],
            ],
            9,
        ),
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            4,
        ),
        (
            [
                ["1", "0", "1", "1", "1"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "0"],
                ["1", "0", "0", "1", "0"],
            ],
            4,
        ),
    ],
)
def test_maximal_square(matrix, expected):
    assert maximal_square(matrix) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
