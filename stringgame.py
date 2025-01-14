s=input()
a=input()

for i in range(len(s)):
    if s[i] not in a:
        print(s[i], end='')
