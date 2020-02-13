from helpers import Timer, sum_proper_divisors


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def abundant_numbers_below(n):
    list_ = []
    for i in range(12, n):
        if sum_proper_divisors(i) > i:
            list_.append(i)
    return list_


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    n = 20161
    abundant_numbers = abundant_numbers_below(n)
    abundant_sums = set()
    for i in abundant_numbers:
        for j in abundant_numbers:
            if i + j <= n:
                abundant_sums.add(i + j)
    ans = set(range(1, n+1)).difference(list(abundant_sums))
    print(sum(ans))
    timer.stop()
