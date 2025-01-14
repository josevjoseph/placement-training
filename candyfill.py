n=int(input())
k=int(input())
rem=n
while(1):
    m=int(input())
    if m>n:
        print("Not Valid")
        continue
    if rem-m<0:
        print("NOT Available")
        continue
    rem=rem-m
    if rem<=k:
        rem+=7
    print("no of candies sold:",m,"No of candies available:",rem)
    