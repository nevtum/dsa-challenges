def longest_common_subsequence(text1: str, text2: str) -> int:
    cache = {}

    def dfs(n: int, m: int, length) -> int:
        res = 0

        for i in range(n, len(text1)):
            for j in range(m, len(text2)):
                if (i, j) in cache:
                    # print(f" cache[({i}, {j})] = {cache[(i, j)]}... already cached")
                    res = cache[(i, j)]
                    continue

                if text1[i] == text2[j]:
                    res = max(res, dfs(i+1, j+1, length+1))
                    cache[(i, j)] = res

        return max(res, length)

    return dfs(0, 0, 0)
