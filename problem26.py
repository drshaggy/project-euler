from helpers import Timer
import copy
import sys


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def calculate_cycle_length(numerator, denominator):
    running = True
    remainder = [numerator % denominator]
    i = 0
    while running:
        while numerator < denominator:
            numerator *= 10
        current_remainder = numerator % denominator
        if current_remainder == 0:
            remainder = [0]
            running = False
        elif current_remainder in remainder:
            running = False
        else:
            remainder.append(current_remainder)
            numerator = current_remainder
    return len(remainder)


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    max_length = 0
    max_num = 0
    for i in range(1, 1000):
        length = calculate_cycle_length(1, i)
        if length > max_length:
            max_length = length
            max_num = i
    print(max_num)
    timer.stop()
