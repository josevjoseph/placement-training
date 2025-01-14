def palindrom(n,a,b):
    count=0

    while a>=0 and b<=len(n)-1 and n[a]==n[b]:
        a-=1
        b+=1
        count+=1
    return count
    
        
n=input()
max=0
char=0
for i in range(len(n)-1):
    len1=palindrom(n,i,i+1)
    len2=palindrom(n,i,i)
    if len1>max:
        max=len1
        char=i
    if len2>max:
        max=len2
        char=i
if n[char]!=n[char+1]:
    
    for i in range(char-max+1,char+max):
        print(n[i], end='')
else:
    
    for i in range(char-max+1,char+max+1):
        print(n[i], end='')



