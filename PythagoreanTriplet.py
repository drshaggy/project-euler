#!/usr/bin/env python
from numpy import sqrt
import time

startTime = time.time()

for a in range(2,1000):
    for b in range(2,1000):
        c = sqrt((a*a)+(b*b))
        if c.is_integer():
            if a + b + c == 1000:
                if a < b:
                    print a*b*c
        else:
            pass

stopTime = time.time()
print "Time Elapsed: %f seconds" % (stopTime - startTime)
