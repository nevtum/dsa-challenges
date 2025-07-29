import heapq
from typing import List


def total_cost(costs: List[int], k: int, candidates: int) -> int:
    if k > len(costs):
        return 0

    n = len(costs)
    low, high = 0, n - 1
    bottom_heap, top_heap = [], []

    total = 0
    for _ in range(k):
        # Fill bottom heap until full
        while len(bottom_heap) < candidates and low <= high:
            heapq.heappush(bottom_heap, costs[low])
            low += 1

        # Then fill top heap until full
        while len(top_heap) < candidates and low <= high:
            heapq.heappush(top_heap, costs[high])
            high -= 1

        # print(bottom_heap, top_heap)
        if not top_heap or (bottom_heap and bottom_heap[0] <= top_heap[0]):
            total += heapq.heappop(bottom_heap)
        else:
            total += heapq.heappop(top_heap)

    return total
