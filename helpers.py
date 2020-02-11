import time


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


# ---------------------------------------------------------
# A class that will time the execution
# ---------------------------------------------------------
class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed = None

    def start(self):
        self.start_time = time.time()
        return self.start_time

    def stop(self):
        if self.start_time:
            self.elapsed = time.time() - self.start_time
            print('Elapsed Time: %.2f seconds' % self.elapsed)
            return self.elapsed
        else:
            print("Timer not started")
