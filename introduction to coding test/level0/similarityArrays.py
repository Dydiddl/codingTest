s1 = ['a', 'b', 'c']
s2 = ['com',  'b', 'd', 'p', 'c']
result = 0

for i in s1:
    for j in s2:
        if i == j:
            result += 1
        else:
            pass
print(result)