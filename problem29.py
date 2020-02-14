from helpers import Timer


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def distinct_powers(lower, upper):
    set_ = set()
    for a in range(lower, upper + 1):
        for b in range(lower, upper + 1):
            set_.add(a ** b)
    return len(list(set_))


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    print(distinct_powers(2, 100))
    timer.stop()