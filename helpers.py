import time
from matplotlib import pyplot as plt
import math


# ---------------------------------------------------------
# Pyplot functions
# ---------------------------------------------------------
def plot_from_file(file):
    with open(file, 'r') as file:
        xs = []
        ys = []
        for line in file:
            x, y = line.split(' ')
            xs.append(int(x))
            ys.append(int(y))
        plt.scatter(xs, ys)
        plt.savefig('plots/problem15.png')


# ---------------------------------------------------------
# Prime Number Functions
# ---------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# ---------------------------------------------------------
# Factor Functions
# ---------------------------------------------------------
def get_factors(n):
    factors = []
    for i in range(1, int((n / 2) + 1)):
        if n % i == 0:
            factors.append(i)
    factors.append(n)
    return factors


def get_prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def sum_proper_divisors(n):
    factors = get_factors(n)[:-1]
    return sum(factors)


# ---------------------------------------------------------
# Algorithms
# ---------------------------------------------------------
def sieve_of_eratosthenes(limit):
    running = True
    primes = [2]
    sieve = set(range(2, limit))
    p = 2
    while running:
        n = 1
        remove = set()
        while n * p < limit:
            remove.add(n * p)
            n += 1
        sieve = sieve.difference(remove)
        try:
            if is_prime(min(sieve)):
                p = min(sieve)
                primes.append(p)
            else:
                running = False
        except ValueError:
            running = False
    primes.sort()
    return primes


# ---------------------------------------------------------
# Sequences
# ---------------------------------------------------------
def fibonacci_sequence(n):
    seq = []
    for i in range(1, n + 1):
        if i == 1 or i == 2:
            seq.append(1)
        elif i == n:
            seq.append((seq[i - 2] + seq[i - 3]))
            return seq
        else:
            seq.append(seq[i - 2] + seq[i - 3])


# ---------------------------------------------------------
# A class that will time the execution
# ---------------------------------------------------------
class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = None

    def start(self):
        self.start_time = time.time()
        return self.start_time

    def stop(self):
        if self.start_time:
            self.elapsed_time = time.time() - self.start_time
            self.start_time = None
            print('Elapsed Time: %.2f seconds' % self.elapsed_time)
            return self.elapsed_time
        else:
            print("Timer not started")

    def elapsed(self):
        if self.start_time:
            self.elapsed_time = time.time() - self.start_time
            print('Elapsed Time: %.2f seconds' % self.elapsed_time)
            return self.elapsed_time
        else:
            print("Timer not started")
