#!/usr/bin env python

import Prime as p
import time




startTime = time.time()
print p.findPrime(10001)
stopTime = time.time()
print "Time Elapsed: %f seconds" % (stopTime - startTime)
