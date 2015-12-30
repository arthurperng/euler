import sys
def palindrome(x):
    x = str(x)
    return x == x[::-1]
biggest = 0
for a in range(999,99,-1):
    for b in range(999,99,-1):
        if palindrome(a * b):
            biggest=max(biggest, a * b)
print biggest





