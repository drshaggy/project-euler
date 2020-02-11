from helpers import Timer


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def collatz_count(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        count += 1
    return count


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    longest_chain = 0
    starting_no = 0
    for i in range(1, 1000000):
        count = collatz_count(i)
        if count > longest_chain:
            longest_chain = count
            starting_no = i
    print(starting_no)
    timer.stop()