from helpers import Timer


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def sum_of_diagonals(size):
    seq = [1]
    n = int(size / 2)
    s = 2
    for i in range(1, n + 1):
        seq.append(seq[-1] + s)
        seq.append(seq[-1] + s)
        seq.append(seq[-1] + s)
        seq.append(seq[-1] + s)
        s += 2
    print(seq)
    return sum(seq)


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    print(sum_of_diagonals(1001))
    timer.stop()