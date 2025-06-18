from collections import deque


def tribonacci(n: int) -> int:
    cache = deque([0, 1, 1])

    if n <= 2:
        return cache[n]

    for i in range(3, n + 1):
        res = sum(cache)
        cache.popleft()
        cache.append(res)

    return cache[-1]
