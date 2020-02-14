from helpers import Timer


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def digit_powers(n):
    list_ = []
    for i in range(n, (n * (9 ** n)) + 1):
        str_ = str(i)
        sum_ = sum([int(c) ** n for c in str_])
        if i == sum_:
            list_.append(i)
    return list_


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    n = 5
    print(digit_powers(n))
    print(sum(digit_powers(n)))
    timer.stop()