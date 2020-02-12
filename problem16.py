from helpers import Timer


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    n = 1000
    prod = 2 ** n
    str_ = str(int(prod))
    sum_ = 0
    for i in str_:
        num = int(i)
        sum_ += num
    print(sum_)
    timer.stop()