from typing import List


def unique_paths_with_obstacles(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    paths = [[0] * m for _ in range(n)]
    paths[0][0] = 1

    # if entry is the same as exit
    if n == m == 1:
        # then check that there is no obstacle
        return 1 if grid[0][0] == 0 else 0

    for i_ref in range(n):
        for j_ref in range(m):
            # if current position is an obstacle, then skip
            if grid[i_ref][j_ref] == 1:
                continue

            # can only travel from up or left position
            for di, dj in ((0, -1), (-1, 0)):
                ii, jj = i_ref + di, j_ref + dj
                # if outside of bounds or travelling from an obstacle
                if ii < 0 or jj < 0 or grid[ii][jj] == 1:
                    continue

                # add different ways to reach paths[ii][jj]
                paths[i_ref][j_ref] += paths[ii][jj]

    return paths[-1][-1]
