import pytest
from .algo import min_distance

@pytest.mark.parametrize("word1,word2,expected", [
    ("", "", 0),
    ("", "a", 1),
    ("a", "", 1),
    ("horse", "ros", 3),
    ("intention", "execution", 5),
])
def test_min_distance(word1, word2, expected):
    assert min_distance(word1, word2) == expected
