from typing import List
import heapq

def min_cost_connect_points(points: List[List[int]]) -> int:
    n = len(points)
    visited = set()

    min_cost = 0
    min_heap = [(0, 0)] # start with first point

    while min_heap:
        # always picks the minimum distance
        dist, i = heapq.heappop(min_heap)

        if i in visited:
            continue

        min_cost += dist
        visited.add(i)
        print(f"Visited point {i}")

        xi, yi = points[i]
        for j in range(i+1, n):
            xj, yj = points[j]
            distance = abs(xi - xj) + abs(yi - yj)
            print(f"Distance from point {i} to point {j}: {distance}")
            heapq.heappush(min_heap, (distance, j))

    return min_cost
