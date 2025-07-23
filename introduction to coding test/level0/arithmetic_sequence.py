a = 3
d = 4
included = [True, False, False, True, True]
arithmetic = []
answer = 0

# for i in range(len(included)):
#     arithmetic.append(3 + 4 * i)

for i in range(len(included)):
    if included[i] :
        answer += a + d * i