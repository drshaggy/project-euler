from helpers import Timer, get_factors


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def sum_factors(n):
    factors = get_factors(n)[:-1]
    return sum(factors)


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    sum_ = 0
    S = []
    for i in range(1, 10001):
        S.append(sum_factors(i))
    for i, s in enumerate(S):
        if sum_factors(s) == i + 1:
            #print(i + 1)
            if sum_factors(s) != s:
                sum_ += (i + 1)
    print(sum_)
   # print(sum_factors(28))
    timer.stop()
