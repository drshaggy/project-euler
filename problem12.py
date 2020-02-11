from helpers import get_factors, Timer, get_prime_factors
from collections import Counter


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def triangle_number(n):
    sum_ = 0
    for i in range(1, n+1):
        sum_ += i
    return sum_


def get_num_factors(n):
    factors = get_prime_factors(n)
    freq = {}
    for factor in factors:
        if factor in freq:
            freq[factor] += 1
        else:
            freq[factor] = 1
    num_factors = 1
    for i in freq:
        num_factors *= freq[i] + 1
    return num_factors


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    max_num_factors = 0
    i = 1
    while max_num_factors < 500:
        tn = triangle_number(i)
        num_factors = get_num_factors(tn)
        if num_factors > max_num_factors:
            max_num_factors = num_factors
        i += 1
    print(max_num_factors)
    print(tn)

    timer.stop()
