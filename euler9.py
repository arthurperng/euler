import sys
for a in range(1, 250):
    for c in range(a+1, 500):
        b=1000-a-c
        if a**2+b**2==c**2:
            print a*b*c
            sys.exit()
