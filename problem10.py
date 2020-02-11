from helpers import *


# ---------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------
def sum_of_primes(limit):
    sum = 2
    i = 3
    while i < limit:
        if is_prime(i):
            sum += i
        i += 2
    return sum


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    print(sum_of_primes(2000000))
    timer.stop()