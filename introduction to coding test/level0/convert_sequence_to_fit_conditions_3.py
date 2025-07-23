arrangement = [1, 2, 3, 100, 99, 98]
k = 2
answer = []
if k % 2:
    for i in arrangement:
        answer.append(i * k)
else:
    for i in arrangement:
        answer.append(i + k)

print(answer)