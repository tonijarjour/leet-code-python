import collections


def numIslands(grid):
    queue = collections.deque()
    count = 0

    for ridx, row in enumerate(grid):
        for iidx, item in enumerate(row):
            found = False
            if item == "1":
                queue.append((ridx, iidx))
                grid[ridx][iidx] = 2
                found = True

            while queue:
                cx, cy = queue.popleft()
                adjecents = ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1))

                for adj in adjecents:
                    jx, jy = adj
                    if (
                        0 <= jx < len(grid)
                        and 0 <= jy < len(row)
                        and grid[jx][jy] == "1"
                    ):
                        grid[jx][jy] = 2
                        queue.append((jx, jy))

            if found:
                count += 1

    return count
