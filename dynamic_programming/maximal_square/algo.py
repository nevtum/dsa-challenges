from typing import List


def maximal_square(matrix: List[List[str]]) -> int:
    n, m = len(matrix), len(matrix[0])
    dp = [[0] * m for _ in range(n)]

    def dfs(i: int, j: int) -> int:
        if i >= n or j >= m or matrix[i][j] == "0":
            return 0

        if dp[i][j] > 0:
            return dp[i][j]

        # we know at this point that size is at least 1
        dp[i][j] = 1

        dirs = (
            (i + 1, j), # down
            (i, j + 1), # right
            (i + 1, j + 1), # diagonal
        )
        neighs = [dfs(ii, jj) for ii, jj in dirs]

        # if neighbour from every direction has non zero size
        # then we can expand the size by 1 at the current position
        if not 0 in neighs:
            dp[i][j] = 1 + min(neighs)

        return dp[i][j]

    max_square = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "0":
                continue
            max_square = max(max_square, dfs(i, j))

    return max_square**2
