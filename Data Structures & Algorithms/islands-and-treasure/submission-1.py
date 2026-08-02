WATER = -1
TREASURE = 0
LAND = 2 ^ 31 - 1


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for i, line in enumerate(grid):
            for j, cell in enumerate(line):
                if not cell == TREASURE:
                    continue

                queue.append(((i, j), 0))

        while queue:
            position, distance = queue.popleft()

            for offset in DIRECTIONS:
                x, y = position[0] + offset[0], position[1] + offset[1]

                if not (0 <= x <= len(grid) - 1 and 0 <= y <= len(grid[0]) - 1):
                    continue

                if grid[x][y] <= distance + 1:
                    continue

                grid[x][y] = distance + 1
                queue.append(((x, y), distance + 1))
