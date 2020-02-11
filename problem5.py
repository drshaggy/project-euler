import time

def isMultiple(x):
    flag = True
    for a in range(21,1,-1):
        if not x % a == 0:
            flag = False
            break
    return flag

def smallestMultiple():
    i=1
    while isMultiple(i) == False:
        i += 1
    return i

startTime = time.time()
print smallestMultiple()
stopTime = time.time()
print "Time Elapsed: %f seconds" % (stopTime - startTime)
