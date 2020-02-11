import time

def checkPalindrome(x):
    string = str(x)
    reverse = string[::-1]
    return string == reverse

def largestPalindromeProduct():
    arr = []
    for a in range(999,99,-1):
        for b in range(999,99,-1):
            x = a*b
            if checkPalindrome(x) == True:
                arr.append(x)
            else:
                pass
    return max(arr)

startTime = time.time()
print largestPalindromeProduct()
stopTime = time.time()
print "Time Elapsed: %f seconds" % (stopTime - startTime)
