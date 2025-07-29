import pytest

from .algo import longest_substring


@pytest.mark.parametrize(
    "s, expected",
    [
        ("", 0),
        ("a", 1),
        ("au", 2),
        ("abcabcbb", 3),
        ("bbbbbb", 1),
        ("xyzaxbcdeoafpzoz", 10),
    ],
)
def test_longest_substring(s, expected):
    assert longest_substring(s) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
