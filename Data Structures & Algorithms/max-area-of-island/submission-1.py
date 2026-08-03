WATER = 0
LAND = 1

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0
        seen = set()

        for i, line in enumerate(grid):
            for j, cell in enumerate(line):
                if grid[i][j] != LAND:
                    continue

                queue = deque()
                queue.append((i, j))
                area = 1

                while queue:
                    r, c = queue.popleft()
                    seen.add((r, c))
                    area += 1

                    # print(r, c)

                    for dr, dc in DIRECTIONS:
                        x, y = r + dr, c + dc

                        if (
                            (x, y) in seen
                            or not (0 < x < len(grid) and 0 < y < len(grid[0]))
                            or grid[x][y] != LAND
                        ):
                            continue

                        queue.append((x, y))

                best = max(best, area)

        return best
