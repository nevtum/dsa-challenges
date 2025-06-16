from functools import cache
from typing import List
from .debug import Tracker

def minimum_total(triangle: List[List[int]]) -> int:
    debug = Tracker()
    height = len(triangle)

    @cache
    @debug.track
    def dp(depth: int, i: int) -> int:
        if depth >= height:
            # if out of bounds, don't add anything
            return 0

        # current node value + best subproblem solution
        res = triangle[depth][i] + min(dp(depth+1, i), dp(depth+1, i+1))
        return res

    return dp(0, 0)
