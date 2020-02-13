from math import factorial
from helpers import Timer


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def sum_digits(n):
    str_ = str(n)
    sum_ = 0
    for i in str_:
        sum_ += int(i)
    return sum_


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    print(sum_digits(factorial(100)))
    timer.stop()