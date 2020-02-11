from Prime import isPrime

def findLargestPrimeFactor(x):
    for b in xrange(2,x-1):
        if x % b == 0:
            if isPrime(x/b) == True:
                pf = x/b
                break
            else:
                pass
        else:
            pass
    return pf

x=13195
y=600851475143

print findLargestPrimeFactor(y)
