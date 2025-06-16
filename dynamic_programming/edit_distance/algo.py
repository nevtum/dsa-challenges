def min_distance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)

    if not word1:
        return m
    if not word2:
        return n

    def dp(i: int, j: int) -> int:
        if i >= n:
            return m - j

        if j >= m:
            return n - i

        if word1[i] == word2[j]:
            # no changes, only calculate sub-problem
            return 0 + dp(i+1, j+1)
        else:
            options = [
                dp(i, j+1), # insert case, no need to move word1 pointer
                dp(i+1, j), # deletion case, no need to move word2 pointer
                dp(i+1, j+1), # replacement case, moving both word1 and word2 pointers
            ]
            # one change plus best sub-problem
            return 1 + min(options)

    return dp(0, 0)
