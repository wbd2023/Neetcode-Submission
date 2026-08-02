WATER = -1
TREASURE = 0
LAND = 2**31 - 1


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        # Append all treasure chests into the queue.
        for i, line in enumerate(grid):
            for j, cell in enumerate(line):
                if cell != TREASURE:
                    continue

                queue.append((i, j))

        min_row, max_row = 0, len(grid) - 1
        min_col, max_col = 0, len(grid[0]) - 1

        # Run multi-source BFS from the treasure chests.
        while queue:
            i, j = queue.popleft()
            distance = grid[i][j] + 1

            for offset in DIRECTIONS:
                x, y = i + offset[0], j + offset[1]

                # Check bounds.
                if not (min_row <= x <= max_row and min_col <= y <= max_col):
                    continue

                # Skip land without a shorter treasure path.
                if grid[x][y] <= distance:
                    continue

                grid[x][y] = distance
                queue.append((x, y))
