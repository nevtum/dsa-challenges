import pytest

from .algo1 import add


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("1+2", 3),
        ("1+2+3", 6),
        ("1+2+3-(4)", 2),
        ("2+(2-3)+4", 5),
        ("18 + (2 - 10 + (1 + 2)) + 4", 17),
    ],
)
def test_add_parameterized(expression, expected):
    assert add(expression) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
