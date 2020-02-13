from helpers import Timer
from itertools import permutations


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    perm = permutations(range(10))
    str_ = ''
    for i in list(perm)[999999]:
        str_ += str(i)
    print(str_)
    timer.stop()