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
