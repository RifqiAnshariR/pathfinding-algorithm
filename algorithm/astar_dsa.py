import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import heapq
import numpy as np
from algorithm.convert_coordinate import cartesianToIndex, indexToCartesian

class OpenSet:
    def __init__(self):
        self.open_set = []  # (cost, index)

    def push(self, cost, index):
        heapq.heappush(self.open_set, (cost, index))

    def pop(self):
        return heapq.heappop(self.open_set)

    def isEmpty(self):
        return len(self.open_set) == 0

class GraphAStar:
    def __init__(self):
        self.came_from = {}

    def calculateHeuristic(self, current_idx, target_idx):
        return abs(current_idx[0] - target_idx[0]) + abs(current_idx[1] - target_idx[1])

    def isValid(self, height, width, grid, neighbor):
        return (0 <= neighbor[0] < height) and (0 <= neighbor[1] < width) and (grid[neighbor] == 0)
    
    def reconstructPath(self, height, start, goal):
        path = []
        current_idx = goal
        while current_idx in self.came_from:
            path.append(indexToCartesian(*current_idx, height))
            current_idx = self.came_from[current_idx]
        path.append(start)
        return path[::-1]

    def aStar(self, grid, start, goal):
        height, width = grid.shape
        start_idx = cartesianToIndex(*start, height)
        goal_idx = cartesianToIndex(*goal, height)

        open_set = OpenSet()
        open_set.push(0, start_idx)

        g_score = {start_idx: 0}

        while not open_set.isEmpty():
            _, current_idx = open_set.pop()

            if current_idx == goal_idx:
                return self.reconstructPath(height, start, goal_idx)

            row, col = current_idx
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Atas, Bawah, Kiri, Kanan
                neighbor = (row + dr, col + dc)

                if self.isValid(height, width, grid, neighbor):
                    tentative_g_score = g_score[current_idx] + 1

                    if (neighbor not in g_score) or (tentative_g_score < g_score[neighbor]):
                        g_score[neighbor] = tentative_g_score
                        f_score = tentative_g_score + self.calculateHeuristic(neighbor, goal_idx)
                        open_set.push(f_score, neighbor)
                        self.came_from[neighbor] = current_idx

        return None
