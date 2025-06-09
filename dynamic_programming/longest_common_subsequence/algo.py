def longest_common_subsequence(text1: str, text2: str) -> int:
    cache = {}

    def dfs(n: int, m: int, length) -> int:
        res = length

        if (n, m) in cache:
            # print(f" cache[({n}, {m})] = {cache[(n, m)]}... already cached")
            return cache[(n, m)]

        for i in range(n, len(text1)):
            for j in range(m, len(text2)):
                if text1[i] == text2[j]:
                    res = max(res, dfs(i+1, j+1, length+1))
                    cache[(i, j)] = res

        return res

    return dfs(0, 0, 0)
