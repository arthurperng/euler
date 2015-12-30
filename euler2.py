a, b=1, 1
number = a+b
while number <= 4000000:
    if number % 2==0:
        sum += number
    a, b=b, number
    number = a+b
print sum