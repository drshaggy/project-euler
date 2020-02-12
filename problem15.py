from helpers import Timer
from math import factorial


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def find_number_of_routes(r):
    n = r * 2
    num = factorial(n) / (factorial(r) * factorial(n - r))
    return num


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    print(int(find_number_of_routes(20)))
    timer.stop()