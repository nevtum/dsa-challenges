def longest_substring(s: str) -> int:
    n = len(s)
    if n <= 1:
        return n

    seen_chars = set()
    low, count = 0, 0

    for high in range(n):
        # remove chars one by one from the start of the string until
        # the only pair of duplicate characters is removed from seen
        while s[high] in seen_chars:
            seen_chars.remove(s[low])
            low += 1

        # then add the char from current high position to seen
        seen_chars.add(s[high])
        count = max(count, high - low + 1)

    return count
