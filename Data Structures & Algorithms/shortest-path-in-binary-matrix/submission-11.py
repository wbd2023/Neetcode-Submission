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

        n, m = size(grid)

        if grid[0][0] == 1 or grid[n][m] == 1:
            return -1

        queue = deque()
        seen = set()

        queue.append(((0, 0), 1))
        seen.add((0, 0))

        while queue:
            pos, length = queue.popleft()

            if pos == (n, m):
                return length

            for offset in self.OFFSETS:
                next = adjacent(grid, pos, offset)

                if next is None:
                    continue

                if grid[next[0]][next[1]] == 1:
                    continue

                if next not in seen:
                    queue.append((next, length + 1))
                    seen.add(next)

        return -1


def display(grid: List[List[int]]) -> None:
    for line in grid:
        print(line)

    print()


def size(grid: List[List[int]]) -> tuple[int, int]:
    return (len(grid) - 1, len(grid[0]) - 1)


def adjacent(
    grid: List[List[int]], pos: tuple[int, int], offset: tuple[int, int]
) -> tuple[int, int] | None:
    n, m = size(grid)

    row = pos[0] + offset[0]
    if row < 0 or row > n:
        return None

    col = pos[1] + offset[1]
    if col < 0 or col > m:
        return None

    return (row, col)
