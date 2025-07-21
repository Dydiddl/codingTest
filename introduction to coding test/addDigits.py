n = 1234

# # 문자열로 변환 해서 문제 해결방법
# sum_list = []
# sum_num = 0
# for i in range(len(str(n))):
#     sum_list.append(str(n)[i])
# for j in sum_list:
#     sum_num += int(j)

# print(sum_num)


# # 정수 n을 그대로 사용해서 문제 해결방법

# sum_num = 0
# if n == 0:
#     # return 0
#     pass
# else:
#     for i in range(len(str(n))):
#         sum_num += n % 10
#         n = n // 10

# print(sum_num)

# 정수 n을 그대로 사용해서 문제 해결방법

sum_num = 0
if n == 0:
    # return 0
    pass
else:
    while n > 0:
        sum_num += n % 10
        # print(sum_num)
        n = n // 10
        # print(n)

print(sum_num)
