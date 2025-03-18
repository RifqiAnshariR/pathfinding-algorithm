import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from algorithm.convert_coordinate import cartesianToIndex, indexToCartesian

class GraphDFS:
    def __init__(self):
        self.came_from = {}

    def isValid(self, height, width, neighbor, grid, visited):
        return (0 <= neighbor[0] < height) and (0 <= neighbor[1] < width) and (grid[neighbor] == 0) and (neighbor not in visited)

    def reconstructPath(self, height, start, goal):
        path = []
        current_idx = goal
        while current_idx in self.came_from:
            path.append(indexToCartesian(*current_idx, height))
            current_idx = self.came_from[current_idx]
        path.append(start)
        return path[::-1]

    def dfs(self, grid, start, goal, visited=None):
        height, width = grid.shape
        start_idx = cartesianToIndex(*start, height)
        goal_idx = cartesianToIndex(*goal, height)

        if visited is None:
            visited = set()

        def _dfs_recursive(current_idx):
            if current_idx == goal_idx:
                return self.reconstructPath(height, start, goal_idx)

            visited.add(current_idx)

            row, col = current_idx
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Atas, Bawah, Kiri, Kanan
                neighbor = (row + dr, col + dc)

                if self.isValid(height, width, neighbor, grid, visited):
                    self.came_from[neighbor] = current_idx
                    result = _dfs_recursive(neighbor)
                    if result:
                        return result

            return None

        return _dfs_recursive(start_idx)

# **Eksekusi DFS dengan grid 5x5**
grid = np.zeros((5, 5), dtype=int)
dfs = GraphDFS()
start = (3, 1)
goal = (4, 4)

path = dfs.dfs(grid, start, goal)
print("Jalur:", path)
