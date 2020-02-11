from helpers import Timer
import numpy as np


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def create_grid(size):
    arr = np.arange((size + 1) * (size + 1)).reshape(size + 1, size + 1)
    return arr


def generate_routes(grid):
    route = grid[0][0]
    for x in range(len(grid[0])):
        for y in range(len(grid[0])):
            pass


class Route:
    def __init__(self, grid):
        self.grid = grid
        self.size = len(grid[0])
        self.x = 0
        self.y = 0

    def get_list_of_legal_moves(self):
        moves = []
        if 0 <= self.x + 1 < self.size:
            moves.append(grid[self.y][self.x + 1])
        if 0 <= self.y + 1 < self.size:
            moves.append(grid[self.y + 1][self.x])
        return moves

    def move(self, x, y):
        self.x = x
        self.y = y
        return grid[y][x]


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    grid = create_grid(2)
    timer.stop()