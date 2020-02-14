from helpers import Timer, is_prime


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def quadratic(n, a, b):
    return (n ** 2) + (a * n) + b

# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    max_number_of_primes = 0
    max_at_a = 0
    max_at_b = 0
    for a in range(-1000, 1000):
        for b in range(-1001, 1001):
            running = True
            n = 0
            while running:
                y = quadratic(n, a, b)
                if is_prime(y):
                    n += 1
                else:
                    running = False
                    if n > max_number_of_primes:
                        max_number_of_primes = n
                        max_at_a = a
                        max_at_b = b
    print(max_at_a * max_at_b)
    print(max_at_a)
    print(max_at_b)
    print(max_number_of_primes)
    timer.stop()