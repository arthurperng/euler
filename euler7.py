primes=[2]
x=3
while len(primes)<10001:
    is_prime = True
    for i in primes:
       if x%i==0:
           is_prime = False
           break
    if is_prime:
        primes.append(x)
    x+=1
print primes