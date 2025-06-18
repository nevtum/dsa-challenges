from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    cheapest_path = cost[:2]

    # O(n) time complexity
    # O(n) storage space, but I could improve it by only keeping last
    # 3 values in cheapest_path, which I didn't bother.
    for i in range(2, len(cost)):
        min_cost = min(cost[i] + cheapest_path[i - 1], cost[i] + cheapest_path[i - 2])
        cheapest_path.append(min_cost)

    # last step comparing last cumulative
    # sum paths and which one is cheapest
    return min(cheapest_path[-2:])
