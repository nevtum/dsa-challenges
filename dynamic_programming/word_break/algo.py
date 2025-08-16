from typing import List


def word_break(s: str, wordDict: List[str], cache={}) -> bool:
    if s in cache:
        return cache[s]

    if s == "":
        return True

    for word in wordDict:
        if not word in s:
            continue

        substring = s.replace(word, "")
        if word_break(substring, wordDict, cache):
            cache[s] = True
            return True

    cache[s] = False
    return False
