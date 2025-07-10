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
        # TODO: try instead comparing len(char_tally.keys()) with sum(char_tally.values())
        while (high < n) and (high - low == count):
            char_tally[s[high]] += 1
            count = max(count, sum(char_tally.values()))
            high += 1

        char_tally[s[low]] -= 1
        low += 1

    return count
