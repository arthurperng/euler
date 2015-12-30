def c(m):
    if m==1:
        return 1
    if m%2==0:
        return c(m/2)+1
    return c(m*3+1)+1
k=0
l=0
for i in range(1, 1000001):
    p=c(i)
    if p>k:
        k=p
        l=i
print l
