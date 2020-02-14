from helpers import Timer


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def calc_next_element(sequence):
    # Calculates next element to fibonacci sequence
    element = sequence[-1] + sequence[-2]
    return element


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    seq = [1, 1]
    index = 2
    num_digits = 0
    while num_digits < 1000:
        next = calc_next_element(seq)
        seq.append(next)
        seq.pop(0)
        index += 1
        num_digits = len(str(next))
    print(index)
    timer.stop()