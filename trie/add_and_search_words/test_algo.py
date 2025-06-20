import pytest

from .algo import WordDictionary


@pytest.fixture()
def word_dictionary() -> WordDictionary:
    wd = WordDictionary()
    wd.addWord("bad");
    wd.addWord("dad");
    wd.addWord("mad");
    return wd

@pytest.mark.parametrize("keyword, expected", [
    ("pad", False),
    ("bad", True),
    (".ad", True),
    ("b..", True),
])
def test_search(word_dictionary, keyword, expected):
    assert word_dictionary.search(keyword) == expected
