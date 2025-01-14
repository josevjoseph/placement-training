


n=input()
k=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyxz"]

newcom=[""]
for digit in n:
    comm=[]
    letters=k[int(digit)]
    for com in newcom:
        for letter in letters:
            comm.append(com+letter)
    newcom=comm

print(newcom)





