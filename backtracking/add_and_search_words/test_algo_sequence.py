import pytest

from .algo import WordDictionary


def test_word_dictionary_sequence():
    # Create a new WordDictionary instance
    wd = WordDictionary()

    # Sequence of operations and expected results
    operations = [
        ("addWord", "at", None),
        ("addWord", "and", None),
        ("addWord", "an", None),
        ("addWord", "add", None),
        ("search", "a", False),
        ("search", ".at", False),
        ("addWord", "bat", None),
        ("search", ".at", True),
        ("search", "an.", True),
        ("search", "a.d.", False),
        ("search", "b.", False),
        ("search", "a.d", True),
        ("search", ".", False)
    ]

    # Perform operations and check results
    for op, arg, expected in operations:
        if op == "addWord":
            wd.addWord(arg)
        elif op == "search":
            assert wd.search(arg) == expected, f"Failed on search({arg})"

if __name__ == "__main__":
    pytest.main([__file__, "-sv"])
