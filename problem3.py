from Prime import isPrime

def find_largest_prime_factor(x):
    for b in range(2,x-1):
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

print(find_largest_prime_factor(y))
