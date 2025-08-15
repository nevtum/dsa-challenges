def num_tilings(n: int) -> int:
    full = [0] * (n + 1)
    full[0] = 1
    full[1] = 1

    upper = [0] * (n + 1)
    lower = [0] * (n + 1)

    for i in range(2, n + 1):
        full[i] = full[i - 1] + full[i - 2] + upper[i - 1] + lower[i - 1]
        upper[i] = lower[i - 1] + full[i - 2]
        lower[i] = upper[i - 1] + full[i - 2]

    return full[n] % (10**9 + 7)
