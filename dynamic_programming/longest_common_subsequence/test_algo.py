import pytest
from .algo import lcs, non_cached_lcs

@pytest.mark.parametrize("text1,text2,expected", [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
    ("oxcpqrsvwf", "shmtulqrypy", 2),
    ("fmtclsfaxchgjavqrifqbkzspazw", "nczivetoxqjclwbwtibqvelwxsdaz", 8)
])
def test_longest_common_subsequence(text1, text2, expected):
    assert non_cached_lcs(text1, text2) == expected
    assert lcs(text1, text2) == expected

@pytest.mark.parametrize("text1,text2,expected", [
    (
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        113,
    ),
])
def test_long_running(text1, text2, expected):
    assert lcs(text1, text2) == expected
