n=int(input())
d={}
while n!=0:
    c=n%10
    if c in d:
        d[c]+=1
    else:
        d[c]=1
    n=n//10
print(d)