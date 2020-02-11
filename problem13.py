from helpers import Timer
import numpy as np


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    with open('data/problem13.txt') as file:
        list_ = []
        for line in file:
            list_.append(int(line))
    print(str(sum(list_))[0:10])
    timer.stop()