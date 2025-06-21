from typing import List
from utils.debug import CallTracker

tracker = CallTracker()

def solve(board: List[List[str]]):
    n, m = len(board), len(board[0])
    visited = {}

    def edge(i: int, j: int) -> bool:
        return i in (0, n-1) or j in (0, m-1)

    def valid(i: int, j: int) -> bool:
        return (0 <= i < n) and (0 <= j < m)

    @tracker.track
    def dfs(i: int, j: int):
        if not valid(i, j) or (i, j) in visited:
            return

        visited[(i, j)] = True

        if board[i][j] == "X":
            return

        # is "O" at this point

        if edge(i, j):
            print(f"found edge at ({i}, {j})")
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                # visit nearby positions adjacent to edge position
                dfs(i + di, j + dj)
        else:
            # breakpoint()
            print(f"found surrounded region at ({i}, {j})")
            board[i][j] = "X"


    for i in range(n):
        for j in range(m):
            # if board[i][j] == "X":
            #     visited[(i, j)] = True
            #     continue

            # # otherwise is "0"
            dfs(i, j)
