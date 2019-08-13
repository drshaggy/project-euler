#!/usr/bin/env python
import time

class Duration:
    startTime = 0
    def start(self):
        startTime = time.time()

    def end(self):
        print " Elapsed time: %f seconds" % time.time() - startTime()
