from typing import List
import heapq

def min_cost_connect_points(points: List[List[int]]) -> int:
    n = len(points)
    visited = set()

    min_cost = 0
    min_heap = [(0, 0)] # start with first point

    # O(n)
    while len(visited) < n:
        # Always pick the minimum distance edge
        dist, i = heapq.heappop(min_heap)

        if i in visited:
            continue

        visited.add(i)
        print(f"Visited point {i}")
        min_cost += dist

        xi, yi = points[i]
        # Explore connections to all unvisited points
        # O(n) * O(n) ~ O(n^2)
        for j in range(n):
            if j in visited:
                continue

            xj, yj = points[j]
            distance = abs(xi - xj) + abs(yi - yj)
            print(f"Distance from point {i} to point {j}: {distance}")
            # O(log n) * O(n^2) ~ O(n^2 log n)
            heapq.heappush(min_heap, (distance, j))

    return min_cost
