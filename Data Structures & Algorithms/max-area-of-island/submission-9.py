WATER = 0
LAND = 1

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class UnionFind:
    def __init__(self, n: int):
        # Each node starts in its own one-node group.
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node: int) -> int:
        # A root represents its group and points to itself.
        if self.parent[node] == node:
            return node

        # Compress the path by pointing this node directly to its root.
        self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, first: int, second: int) -> None:
        # Find the roots representing each node's group.
        first_root = self.find(first)
        second_root = self.find(second)

        # Nothing changes if both nodes are already in the same group.
        if first_root == second_root:
            return

        # Attach the smaller group to the larger one to keep the tree shallow.
        if self.size[first_root] < self.size[second_root]:
            first_root, second_root = second_root, first_root

        self.parent[second_root] = first_root
        self.size[first_root] += self.size[second_root]

    def getSize(self, node: int) -> int:
        # Group sizes are maintained at their roots.
        root = self.find(node)
        return self.size[root]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Represent each grid cell as a node in the union-find structure.
        groups = UnionFind(rows * cols)
        best = 0

        def index(r: int, c: int) -> int:
            # Flatten the grid position into a unique node index.
            return r * cols + c

        for i, line in enumerate(grid):
            for j, cell in enumerate(line):
                if cell != LAND:
                    continue

                # Merge this cell with every adjacent land cell.
                for dr, dc in DIRECTIONS:
                    r, c = i + dr, j + dc

                    if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != LAND:
                        continue

                    groups.union(index(i, j), index(r, c))

                # Each island is one group, whose size is its area.
                best = max(best, groups.getSize(index(i, j)))

        return best
