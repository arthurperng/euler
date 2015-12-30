numbers=range(2, 2000000)
import math
primes=[]
while numbers[0]<math.sqrt(2000000):
    x=numbers[0]
    numbers = [i for i in numbers if i%x!=0]
    print x
    primes.append(x)

print sum(primes+numbers)