r=int(input())
unit=int(input())
n=int(input())
arr=[0 for i in range(n)]
for i in range(n):
    arr[i]=int(input())
total=r*unit
sum=0
for i in range(n):
    sum=sum+arr[i]
    if sum>=total:
        break
print(i+1)