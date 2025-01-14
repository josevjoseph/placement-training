n=int(input())
k=int(input())
j=int(input())
m=int(input())
p=int(input())
if k==0 or j==0:
    print("INVALID INPUT")
    exit(0)

num=((m//k)+(p//j))%n
monkeys=n-num
if m%k or p%j:
    monkeys-=1
print(monkeys)