import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from algorithm.convert_coordinate import cartesianToIndex, indexToCartesian
from collections import deque

class GraphBFS:
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

    def bfs(self, grid, start, goal):
        height, width = grid.shape
        start_idx = cartesianToIndex(*start, height)
        goal_idx = cartesianToIndex(*goal, height)

        visited = set()
        queue = deque([start_idx])
        visited.add(start_idx)

        while queue:
            node = queue.popleft()

            if node == goal_idx:
                return self.reconstructPath(height, start, goal_idx)

            row, col = node
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Atas, Bawah, Kiri, Kanan
                neighbor = (row + dr, col + dc)

                if self.isValid(height, width, neighbor, grid, visited):
                    visited.add(neighbor)
                    queue.append(neighbor)
                    self.came_from[neighbor] = node

        return None
