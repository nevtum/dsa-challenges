from functools import cache
from typing import List
# from .debug import Tracker

def minimum_total(triangle: List[List[int]]) -> int:
    # debug = Tracker()
    height = len(triangle)

    @cache
    # @debug.track
    def dp(depth: int, i: int) -> float:
        if not (0 <= depth < height) or not (0 <= i < len(triangle[depth])):
            return float("inf")

        if depth >= height-1:
            # if bottom of the triangle, return current
            return triangle[depth][i]

        # current node value + best subproblem solution
        res = triangle[depth][i] + min(dp(depth+1, i), dp(depth+1, i+1))
        return res

    return int(dp(0, 0))
