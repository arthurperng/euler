from math import sqrt

def is_prime_to(n, primes):
    for x in primes:
        if n % x==0:
            return False
    primes.append(n)
    return True

primes=[]
for x in range(2,int(sqrt(600851475143))):
    if is_prime_to(x, primes):
        if 600851475143 % x==0:
            print primes
            print x
