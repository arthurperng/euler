import math
def divisors2(x):
    f=math.sqrt(x)
    j=0
    for i in range (1, int(math.sqrt(x))):
        if x%i==0:
            j+=2
    if math.sqrt(x)==int(math.sqrt(x)):
        j-=1
    return j
x=1
total=0
while True:
    total+=x
    x+=1
    d=divisors2(total)
    if divisors2(total)>=500:
        print total
        break
