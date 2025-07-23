num_list = [3, 4, 5, 2, 1]
num_mul = 1
num_sum = sum(num_list)
answer = 0

# first 풀이
for i in num_list:
    num_mul *= i

if num_mul < num_sum ** 2:
    answer = 1
else:
    answer = 0

print(answer)