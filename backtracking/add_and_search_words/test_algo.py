import pytest

from .algo import WordDictionary


@pytest.fixture()
def word_dictionary() -> WordDictionary:
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    wd.addWord("mid")
    return wd


@pytest.mark.parametrize(
    "keyword, expected",
    [
        ("pad", False),
        ("bad", True),
        (".id", True),
        ("..d", True),
        ("..c", False),
        ("b..", True),
        (".", True),
    ],
)
def test_search(word_dictionary, keyword, expected):
    assert word_dictionary.search(keyword) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
