import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithm.bfs_dsa import GraphBFS
from algorithm.dfs_dsa import GraphDFS
from algorithm.astar_dsa import GraphAStar

from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt Basic Window")
        self.setGeometry(100, 100, 400, 300)  # (x, y, width, height)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())

graph = GraphBFS()
