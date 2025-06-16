from typing import List
from functools import cache

def min_path_sum(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])

    @cache
    def dp(i: int, j: int) -> float:
        # when outside the grid
        if not (0 <= i < n and 0 <= j < m):
            return float('inf')

        # Base case: when position has reached the bottom-right
        if i == n-1 and j == m-1:
            return grid[i][j]

        # current position + min path from either right or down
        return grid[i][j] + min(dp(i+1,j), dp(i,j+1))

    return int(dp(0, 0))
