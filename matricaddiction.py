m=int(input())
n=int(input())
p=int(input())
q=int(input())
a=[[0 for i in range(n)] for i in range(m)]
b=[[0 for i in range(q)] for i in range(p)]
c=[[0 for i in range(n)] for i in range(m)]
for i in range(m):
   
    for j in range(n):
        
        a[i][j]=int(input())
for i in range(p):
   
    for j in range(q):
        
        b[i][j]=int(input())
if m==p and n==q:
    for i in range(m):
        for j in range(n):
            c[i][j]=a[i][j]+b[i][j]
    print(c)
else:
    print("addition not possible")


