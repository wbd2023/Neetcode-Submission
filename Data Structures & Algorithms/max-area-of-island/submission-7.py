WATER = 0
LAND = 1

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        best = 0
        seen = set()

        for i, line in enumerate(grid):
            for j, cell in enumerate(line):
                if cell != LAND or (i, j) in seen:
                    continue

                # Start a new island and count its first land cell.
                queue = deque([(i, j)])
                seen.add((i, j))
                area = 1

                while queue:
                    r, c = queue.popleft()

                    for dr, dc in DIRECTIONS:
                        x, y = r + dr, c + dc

                        if (
                            (x, y) in seen
                            or not (0 <= x < rows and 0 <= y < cols)
                            or grid[x][y] != LAND
                        ):
                            continue

                        # Mark cells as seen when queued so duplicates are not counted towards the area.
                        queue.append((x, y))
                        seen.add((x, y))
                        area += 1

                best = max(best, area)

        return best
