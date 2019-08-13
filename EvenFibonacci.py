def generateFibinacci(elements):
    #Generate Finonacci sequence to a number of elements
    if elements == 1:
        seq = [1]
        return seq
    elif elements == 2:
        seq = [1,2]
        return seq
    else:
        seq = [1,2]
        for x in range(elements-2):
            next = calcNextElement(seq)
            seq.append(next)
        return seq

def calcNextElement(sequence):
    #Calculates next element to fibonacchi sequence
    size = len(sequence)
    element = sum([sequence[size-2],sequence[size-1]])
    return element


def calcFibonacciTo(number):
    a = 1
    i = 0
    while i <= number:
        arr = generateFibinacci(a)
        i = max(arr)
        a += 1
        arr.pop()
    return arr

def getEvenSubset(arr):
    even = []
    for x in arr:
        if x % 2 == 0:
            even.append(x)
        else:
            pass
    return even


print sum(getEvenSubset(calcFibonacciTo(4000000)))
