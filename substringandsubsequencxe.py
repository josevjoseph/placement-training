






def find_subsequences(s):
    result = [""]
    for char in s:
        result += [char + sub for sub in result]
    return result

# Example with a given string

s = input("Enter a string: ")

substr=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        substr.append(s[i:j])
subsequences = find_subsequences(s)
print("All Subsequences:", subsequences,"\nsub string :",substr)



