WATER = 0
LAND = 1

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        display(grid)

        best = 0
        seen = set()

        for i, line in enumerate(grid):
            for j, cell in enumerate(line):
                if grid[i][j] != LAND or (i, j) in seen:
                    continue

                queue = deque()

                queue.append((i, j))
                seen.add((i, j))
                area = 1

                while queue:
                    r, c = queue.popleft()

                    # print(r, c, queue, area)
                    # print(seen)
                    # print()

                    for dr, dc in DIRECTIONS:
                        x, y = r + dr, c + dc

                        if (
                            (x, y) in seen
                            or not (0 <= x <= len(grid) - 1 and 0 <= y <= len(grid[0]) - 1)
                            or grid[x][y] != LAND
                        ):
                            continue

                        queue.append((x, y))
                        seen.add((x, y))
                        area += 1

                best = max(best, area)

        return best


def display(grid: List[List[int]]) -> None:
    for line in grid:
        print(line)

    print()
