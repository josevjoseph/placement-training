n=int(input())
arr=[]
odd=[]
even=[]
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in range(n):
    if i%2==0:
        odd.append(arr[i])
    else:
        even.append(arr[i])

print(odd)
print(even)
print(odd[-2]+even[-2])