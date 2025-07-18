from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    n, m = len(matrix), len(matrix[0])
    dp = [[0] * m for _ in range(n)]

    def dfs(i: int, j: int) -> int:
        if i >= n or j >= m or matrix[i][j] == "0":
            return 0

        if dp[i][j] > 0:
            return dp[i][j]

        dirs = (
            (i + 1, j),  # down
            (i, j + 1),  # right
            (i + 1, j + 1),  # diagonal
        )

        # calc size from every direction then
        # expand the size by 1 at the current position
        # by the neighbour which has the minimum
        dp[i][j] = 1 + min([dfs(ii, jj) for ii, jj in dirs])

        return dp[i][j]

    max_square = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "0":
                continue
            max_square = max(max_square, dfs(i, j))

    return max_square**2
