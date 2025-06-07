from .v1 import letter_combinations
import pytest

@pytest.mark.parametrize("digits,expected", [
    ("", []),
    ("2", ['a', 'b', 'c']),
    ("23", ['ad','ae','af','bd','be','bf','cd','ce','cf']),
])
def test_letter_combs(digits, expected):
    assert letter_combinations(digits) == expected
