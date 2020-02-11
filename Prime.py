#!/usr/bin env python

def isPrime(x):
    flag = True
    for a in range(2, x - 1):
        if x % a == 0:
            flag = False
            break
        else:
            pass
    return flag


def findPrime(x):
    numOfPrimes = 0
    num = 1
    while numOfPrimes != x + 1:
        if isPrime(num) == True:
            lastPrime = num
            numOfPrimes += 1
        else:
            pass
        num += 1
    return lastPrime


def findPrimesBelow(x):
    lastPrime = 0
    num = 1
    arr = []
    while lastPrime < x:
        print(num)
        if isPrime(num) == True:
            lastPrime = num
            arr.append(num)
        else:
            pass
        num += 1
    return arr[0:len(arr) - 1]
