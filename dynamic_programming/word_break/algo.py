from typing import List


def word_break(s: str, wordDict: List[str], cache={}) -> bool:
    if s in cache:
        return cache[s]

    if s == "":
        return True

    for i in range(1, len(s) + 1):
        for word in wordDict:
            if word == s[:i]:
                next_word = s[i:]
                if word_break(next_word, wordDict, cache):
                    cache[s] = True
                    return True

    cache[s] = False
    return False
