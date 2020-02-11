import time

def squareSum(x):
    sum = 0
    for i in range(1,x+1):
        sum += i*i
    return sum

def sumSquare(x):
    sum = 0
    for i in range(1,x+1):
        sum += i
    return sum*sum

def sumSquareDiff(x):
    a = squareSum(x)
    b = sumSquare(x)
    return b - a

startTime = time.time()
print sumSquareDiff(100)
stopTime = time.time()
print "Time Elapsed: %f seconds" % (stopTime - startTime)
