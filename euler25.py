a, b=1, 1
term=3
number = a+b
while len(str(number))<1000:
    term+=1
    a, b=b, number
    number = a+b
print term
