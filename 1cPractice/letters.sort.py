sec = "aaabbccccdaa"
s1 = sec[0]
count = 0
result = ''
# print(s1)
for i in sec:
    if i == s1:
        count +=1
    else:
        result += s1+str(count)
        s1 = i
        count = 1
result += s1+str(count)
print(result)
