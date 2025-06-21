from typing import List
from collections import deque


def solve(board: List[List[str]]):
    n, m = len(board), len(board[0])
    visited = {}
    q = deque()

    def edge(i: int, j: int) -> bool:
        return i in (0, n-1) or j in (0, m-1)

    def valid(i: int, j: int) -> bool:
        return (0 <= i < n) and (0 <= j < m)

    def dfs_mark_invalid(i: int, j: int):
        if not valid(i, j) or (i, j) in visited:
            return

        visited[(i, j)] = True

        if board[i][j] == "X":
            return

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            # visit nearby positions adjacent to edge position
            dfs_mark_invalid(i + di, j + dj)

    for i in range(n):
        for j in range(m):
            if board[i][j] == "O" and edge(i, j):
                dfs_mark_invalid(i, j)
            elif board[i][j] == "X":
                visited[(i, j)] = True
            else:
                # candidates to be flipped
                q.append((i, j))

    while q:
        i, j = q.popleft()
        if (i, j) not in visited:
            # flip those not visited
            board[i][j] = "X"
