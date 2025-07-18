from typing import List


def is_valid(seq: List[str]) -> bool:
    exists = set()

    for val in seq:
        if val.isdigit() and val in exists:
            return False
        exists.add(val)

    return True


def is_valid_sudoku(board: List[List[str]]) -> bool:
    n = len(board)

    for i in range(0, n, 3):
        for j in range(0, n, 3):
            square = [board[x + i][y + j] for x in range(3) for y in range(3)]
            if not is_valid(square):
                return False

    for i in range(n):
        row = board[i]
        if not is_valid(row):
            return False

        col = [board[j][i] for j in range(n)]
        if not is_valid(col):
            return False

    return True
