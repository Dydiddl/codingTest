myString = "ABAB"
pat = "ABAB"
newMyString = ''
answer = 0
for i in myString:
    if i == 'A':
        newMyString += 'B'
    else:
        newMyString += 'A'
print(newMyString)
if newMyString.find(pat) == -1:
    answer = 0
else:
    answer += 1

print(answer)