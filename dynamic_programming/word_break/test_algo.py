import pytest
from .algo import word_break


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("", ["doesn't", "matter"], True),
        ("a", ["b"], False),
        ("ccbb", ["bc", "cb"], False),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ],
)
def test_word_break(s, words, expected):
    assert word_break(s, words) == expected


if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
