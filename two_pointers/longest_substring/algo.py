from collections import defaultdict

def longest_substring(s: str) -> int:
    n = len(s)
    if n <= 1:
        return n

    low, high, count = 0, 1, 1
    char_tally = defaultdict(int)
    char_tally[s[low]] += 1

    while low < n:
        assert low <= high, f"{low} <= {high}"
        while (high < n) and len(char_tally.keys()) == sum(char_tally.values()):
            count = max(count, sum(char_tally.values()))
            char_tally[s[high]] += 1
            high += 1

        if len(char_tally.keys()) == sum(char_tally.values()):
            count = max(count, sum(char_tally.values()))

        char_tally[s[low]] -= 1
        if char_tally[s[low]] == 0:
            del char_tally[s[low]]
        low += 1

    return count
