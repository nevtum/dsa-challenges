def unique_paths(n: int, m: int) -> int:
    paths = [[0] * m for _ in range(n)]
    paths[0][0] = 1

    # can only come from up or left directions
    directions = [(-1, 0), (0, -1)]
    for i_ref in range(n):
        for j_ref in range(m):
            for di, dj in directions:
                i, j = i_ref + di, j_ref + dj
                # outside of grid
                if i < 0 or j < 0:
                    continue

                paths[i_ref][j_ref] += paths[i][j]

    # get value from bottom-right position
    return paths[-1][-1]
