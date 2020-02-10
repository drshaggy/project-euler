from helpers import *


timer = Timer()


def sum_of_primes(limit):
    sum = 2
    i = 3
    while i < limit:
        if is_prime(i):
            sum += i
        i += 2
    return sum


if __name__ == "__main__":
    timer.start()
    print(sum_of_primes(2000000))
    timer.stop()