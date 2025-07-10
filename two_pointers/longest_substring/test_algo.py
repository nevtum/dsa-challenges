import pytest
from .algo import longest_substring

@pytest.mark.parametrize("s, expected", [
    ("abcabcbb", 3),
    ("bbbbbb", 1),
])
def test_longest_substring(s, expected):
    assert longest_substring(s) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
