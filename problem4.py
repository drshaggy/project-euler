from helpers import Timer


# ---------------------------------------------------------
# Helper Methods
# ---------------------------------------------------------
def is_palindrome(x):
    string = str(x)
    reverse = string[::-1]
    return string == reverse


def largest_palindrome_product():
    arr = []
    for a in range(999,99,-1):
        for b in range(999,99,-1):
            x = a*b
            if is_palindrome(x):
                arr.append(x)
            else:
                pass
    return max(arr)


# ---------------------------------------------------------
# Execution
# ---------------------------------------------------------
if __name__ == "__main__":
    timer = Timer()
    startTime = timer.start()
    print(largest_palindrome_product())
    timer.stop()
