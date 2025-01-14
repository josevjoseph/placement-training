size=int(input())
a=[]
for i in range(size):
    a.append(int(input()))
rot=int(input())%size
a=a[rot:]+a[:rot]
print(a)