from typing import List

from utils.debug import CallTracker

tracker = CallTracker()


def number_of_islands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = {}
    islands = 0

    def valid(i: int, j: int) -> bool:
        return (0 <= i < rows) and (0 <= j < cols)

    @tracker.track
    def dfs(i: int, j: int):
        if not valid(i, j):
            return
        if (i, j) in visited:
            return
        if grid[i][j] == "0":
            return

        # At this point we are on new land
        visited[(i, j)] = True

        # Recursively visit land around current position
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dfs(i + di, j + dj)

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and (i, j) not in visited:
                print(f"Starting DFS from ({i}, {j})")
                # count every land not visited
                islands += 1
                # Fully explore connecting land from this position
                dfs(i, j)

    return islands
