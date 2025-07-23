n = 10
sum = 0


# 처음 바로 생각든 코드
if not n % 2:
    for i in range(2, n+1, 2):
        sum += i**2
else:
    for i in range(1, n+1, 2):
        sum += i


# 새로운 해결방법 생각 해보기



print(sum)

print(bool(1))
print(bool(0))
