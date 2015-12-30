def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def lcm(a, b):
    return a * b / gcd(a, b)
common = 1
for x in range(1, 21, 1):
    common=lcm(common, x)
    print x,common
print common


