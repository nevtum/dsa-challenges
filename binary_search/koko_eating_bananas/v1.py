from typing import List
import math

def min_eating_speed_brute_force(piles: List[int], h: int) -> int:
    # O(n)
    min_speed = 1
    max_speed = max(piles)+ 1

    # O(n)
    for speed in range(min_speed, max_speed):
        total_hours = sum((math.ceil(pile/speed) for pile in piles))

        print(f"speed={speed}, total_hours={total_hours}, h={h}")
        if total_hours <= h:
            return speed

    return -1


def min_eating_speed_binary_search(piles: List[int], h: int) -> int:
    def in_time(rate):
        total_hours = sum((math.ceil(pile/rate) for pile in piles))

        # both before or on time is sufficient
        return total_hours <= h

    # O(n)
    low, high = 1, max(piles)

    while low != high:
        rate = (low + high) // 2

        if in_time(rate):
            high = rate
        else:
            low = rate + 1

        # print(f"rate={rate}, total_hours={total_hours}, h={h}, range=[{low}, {high}]")

    # assert low == high
    return low
