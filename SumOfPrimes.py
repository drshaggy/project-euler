#!/usr/bin/env python
import Prime as p
import time

startTime = time.time()
print p.findPrimesBelow(2000000)
stopTime = time.time()
print "Time Elapsed: %f seconds" % (stopTime - startTime)
