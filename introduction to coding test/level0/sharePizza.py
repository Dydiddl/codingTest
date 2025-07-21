import math
slice = 7 # 피자 조각의 수
n = 10 # 나눠 먹을 사람의 수

# 2 <= slice <= 10
# 1<= n <= 100

print(math.ceil(n / slice))

print(((n - 1) // slice) + 1)