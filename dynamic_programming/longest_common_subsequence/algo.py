def non_cached_lcr(text1: str, text2: str) -> int:
    def dfs(n: int, m: int, length) -> int:
        res = length

        for i in range(n, len(text1)):
            for j in range(m, len(text2)):
                if text1[i] == text2[j]:
                    print(f"({i}, {j}) -> {length}")
                    res = max(res, dfs(i+1, j+1, length+1))

        return res

    return dfs(0, 0, 0)


def lcr(text1: str, text2: str) -> int:
    cache = {}
    n, m = len(text1), len(text2)

    def dfs(i: int, j: int) -> int:
        # Base case
        if i >= n or j >= m:
            return 0

        if (i, j) in cache:
            return cache[(i, j)]

        res = 0
        if text1[i] == text2[j]:
           res = 1 + dfs(i+1, j+1)
        else:
            # try varying index of text1 or index of text2
            res = max(dfs(i+1, j), dfs(i, j+1))

        cache[(i, j)] = res
        return res

    return dfs(0, 0)
