n=int(input())
energy=int(input())
p=[]
g=[]
for i in range(n):
    p.append(int(input()))
for i in range(n):
    g.append(int(input()))
sum=0
while any(energy>=power for power in p):
    ele=0
    for i in range(len(p)):
        if energy>=p[i]:
            break
    energy+=g[i]
    p.pop(i)
    g.pop(i)
    sum+=1
print(sum)

    
    
            
        


