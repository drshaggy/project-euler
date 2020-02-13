from helpers import Timer, sum_proper_divisors


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    sum_ = 0
    S = []
    for i in range(1, 10001):
        S.append(sum_proper_divisors(i))
    for i, s in enumerate(S):
        if sum_proper_divisors(s) == i + 1:
            if sum_proper_divisors(s) != s:
                sum_ += (i + 1)
    print(sum_)
    timer.stop()
