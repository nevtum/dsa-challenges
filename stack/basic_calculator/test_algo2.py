import pytest

from .algo2 import evaluate


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("1+2", 3),
        ("1+2+3", 6),
        ("1+2+3-(4)", 2),
        ("2+(2-3)+4", 5),
        ("18 + (2 - 10 + (1 + 2)) + 4", 17),
        ("2^2", 4),
        ("2^(4-1)", 8),
        ("2^(8-(4+2))-3", 1),
        ("2*5", 10),
        ("2^(3*2)", 64),
        ("2^3*2", 16),
        ("3*(2^3)", 24),
        ("3*2^3", 24),
    ],
)
def test_add_parameterized(expression, expected):
    assert evaluate(expression) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
