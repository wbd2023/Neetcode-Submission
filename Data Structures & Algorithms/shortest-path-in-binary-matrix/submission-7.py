class Solution:
    OFFSETS = [
        # Top-left to bottom-right (excl. middle).
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        # (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        display(grid)

        n = len(grid) - 1
        m = len(grid[0]) - 1

        if grid[0][0] == 1 or grid[n][m] == 1:
            return -1

        seen = set()
        queue = deque()

        queue.append(((0, 0), 1))

        while queue:
            pos, length = queue.popleft()
            seen.add(pos)

            for offset in self.OFFSETS:
                next = adjacent(grid, pos, offset)

                if not next:
                    continue

                if grid[next[0]][next[1]] == 1:
                    continue

                if next == (n, m):
                    return length + 1

                if next not in seen:
                    queue.append((next, length + 1))

        return -1


def display(grid: List[List[int]]) -> None:
    for line in grid:
        print(line)

    print()


def adjacent(
    grid: List[List[int]], pos: tuple[int, int], offset: tuple[int, int]
) -> tuple[int, int] | None:
    row = pos[0] + offset[0]
    if row < 0 or row > len(grid) - 1:
        return None

    col = pos[1] + offset[1]
    if col < 0 or col > len(grid[0]) - 1:
        return None

    return (row, col)
