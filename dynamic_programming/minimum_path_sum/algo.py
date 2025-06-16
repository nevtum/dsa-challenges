from typing import List

def min_path_sum(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    print(f"{n}x{m}")

    def valid(i: int, j: int) -> bool:
        return 0 <= i < n and 0 <= j < m

    def dp(i: int, j: int) -> int:
        if not valid(i, j):
            return 0

        best = float('inf')
        valid_dir = False

        # right or down
        for di, dj in ((0, 1),(1, 0)):
            ii, jj = i+di, j+dj
            if valid(ii, jj):
                valid_dir = True
                best = min(best, dp(ii, jj))

        if not valid_dir:
            return grid[i][j]
        else:
            return grid[i][j] + int(best)

    return dp(0, 0)
