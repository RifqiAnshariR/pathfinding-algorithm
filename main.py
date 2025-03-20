import numpy as np

from algorithm.astar_dsa import GraphAStar
from algorithm.bfs_dsa import GraphBFS
from algorithm.dfs_dsa import GraphDFS

def run_search_algorithms(grid, start, goal):
    astar = GraphAStar()
    bfs = GraphBFS()
    dfs = GraphDFS()

    astar_path = astar.aStar(grid, start, goal)
    bfs_path = bfs.bfs(grid, start, goal)
    dfs_path = dfs.dfs(grid, start, goal)

    print("Jalur AStar:", astar_path)
    print("Jalur BFS:", bfs_path)
    print("Jalur DFS:", dfs_path)

if __name__ == "__main__":
    grid = np.zeros((5, 5), dtype=int)
    start = (2, 1)
    goal = (4, 4)

    run_search_algorithms(grid, start, goal)
