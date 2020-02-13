from helpers import Timer

# ------
# ---------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def isMultiple(x):
    flag = True
    for a in range(21,1,-1):
        if not x % a == 0:
            flag = False
            break
    return flag


def smallestMultiple():
    i = 1
    while isMultiple(i) == False:
        i += 1
    return i


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    timer.start()
    print(smallestMultiple())
    timer.stop()

