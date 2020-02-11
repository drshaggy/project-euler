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


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    grid = create_grid(2)
    timer.stop()