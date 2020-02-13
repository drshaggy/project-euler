from helpers import Timer, fibonacci_sequence


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    list_ = fibonacci_sequence(12)
    print(list_)
    timer.stop()