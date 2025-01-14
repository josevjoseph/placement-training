m=int(input())
n=int(input())
a=[[0 for i in range(n)] for i in range(m)]
for i in range(m):
   
    for j in range(n):
        
        a[i][j]=int(input())
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print("")
