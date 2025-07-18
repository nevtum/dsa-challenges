from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    n, m = len(matrix), len(matrix[0])
    dp = [[0] * m for _ in range(n)]

    def dfs(i: int, j: int) -> int:
        if matrix[i][j] == "0":
            return 0

        if dp[i][j] > 0:
            return dp[i][j]

        edges = (
            (i + 1, j),
            (i, j + 1),
            (i + 1, j + 1),
        )
        for ii, jj in edges:
            if ii >= n or jj >= m:
                return 1

        neighs = [dfs(ii, jj) for ii, jj in edges]
        if 0 in neighs:
            dp[i][j] = 1
        else:
            dp[i][j] = 1 + min(neighs)

        return dp[i][j]

    max_square = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "0":
                continue
            max_square = max(max_square, dfs(i, j))

    return max_square**2
