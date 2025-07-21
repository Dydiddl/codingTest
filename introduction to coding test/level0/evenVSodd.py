num_list = [4, 2, 6, 1, 7, 6]
# 첫 번째 원소를 1번 원소, 따라서 0 -> 1 1-> 2 홀짝의 구분이 반대임
answer = 0
even_sum = 0
odd_sum = 0

for i in range(len(num_list)):
    if i % 2 == 0:
        odd_sum += num_list[i]
    else:
        even_sum += num_list[i]
if even_sum >= odd_sum:
    answer = even_sum
else:
    answer = odd_sum


# 함수를 이용해서 풀이

answer = max(sum(num_list[::2]), sum(num_list[1::2]))