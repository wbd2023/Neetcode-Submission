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

                up = grid[row - 1][col] if (not row == 0) and (grid[row - 1][col] > 0) else None
                left = grid[row][col - 1] if (not col == 0) and (grid[row][col - 1] > 0) else None
                diag = (
                    grid[row - 1][col - 1]
                    if (not row == 0 and not col == 0) and (grid[row - 1][col - 1] > 0)
                    else None
                )

                prevs = [up, left, diag]

                # print(f"[up, left, diag] = {[up, left, diag]}")
                # print(any(prevs))

                if any(prevs):
                    grid[row][col] = min(filter(lambda x: x is not None, prevs)) + 1

                # display(grid)

        return grid[max_row][max_col] if not grid[max_row][max_col] == 0 else -1


def display(grid: List[List[int]]) -> None:
    for line in grid:
        print(line)

    print()


def normalise(grid: List[List[int]]) -> None:
    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell == 1:
                grid[row][col] = -1
            elif row == 0 and col == 0:
                grid[0][0] = 1
