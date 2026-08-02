WATER = -1
TREASURE = 0
LAND = 2 ^ 31 - 1


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        # Append all treasure chests into the queue.
        for i, line in enumerate(grid):
            for j, cell in enumerate(line):
                if not cell == TREASURE:
                    continue

                queue.append(((i, j), 0))

        min_row, max_row = 0, len(grid) - 1
        min_col, max_col = 0, len(grid[0]) - 1

        # Run multi-source BFS from the treasure chests.
        while queue:
            position, distance = queue.popleft()

            distance += 1
            for offset in DIRECTIONS:
                x, y = position[0] + offset[0], position[1] + offset[1]

                # Check bounds.
                if not (min_row <= x <= max_row and min_col <= y <= max_col):
                    continue

                # Check for a shorter treasure path to this land cell.
                if grid[x][y] <= distance:
                    continue

                grid[x][y] = distance
                queue.append(((x, y), distance))
