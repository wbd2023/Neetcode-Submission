class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1

        normalise(grid)
        display(grid)

        for row, line in enumerate(grid):
            for col, cell in enumerate(line):
                if not cell == 0:
                    continue

                pos = (row, col)
                up = get_prev(grid, pos, (-1, 0))
                left = get_prev(grid, pos, (0, -1))
                diag = get_prev(grid, pos, (-1, -1))
                prevs = [up, left, diag]

                if any(prevs):
                    grid[row][col] = min(filter(lambda x: x is not None, prevs)) + 1

                # display(grid)

        return grid[max_row][max_col] if not grid[max_row][max_col] == 0 else -1


def normalise(grid: List[List[int]]) -> None:
    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell == 1:
                grid[row][col] = -1
            elif row == 0 and col == 0:
                grid[0][0] = 1


def display(grid: List[List[int]]) -> None:
    for line in grid:
        print(line)

    print()


def get_prev(grid: List[List[int]], pos: tuple[int, int], offset: tuple[int, int]) -> int | None:
    row = pos[0] + offset[0]
    if row < 0:
        return None

    col = pos[1] + offset[1]
    if col < 0:
        return None

    prev = grid[row][col]
    return prev if prev > 0 else None
