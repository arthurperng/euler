c=[[0]*21 for i in range(21) ]


for i in range(21):
    c[i][20]=1
    c[20][i]=1
for i in range(19, -1, -1):
    for j in range(19, -1, -1):
        c[i][j]=c[i+1][j]+c[i][j+1]
        print i, j, c[i][j]