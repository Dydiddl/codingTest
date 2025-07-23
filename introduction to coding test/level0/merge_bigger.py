a = 12
b = 3


# # 가장 먼저 떠오른 해답
# if int(str(a) + str (b)) > int(str(b) + str (a)):
#     answer = int(str(a) + str (b))
# else : 
#     answer = int(str(b) + str (a))


# 중복되는 것을 해결 해보자
# 이렇게 하면 a + b, b + a 를 최초에 한번만 계산하면 됨
# 위의 해답은 총 3번의 계산이 이루어짐
sum_string_a =int(str(a) + str(b))
sum_string_b = int(str(b) + str(a))
if sum_string_a > sum_string_b:
    answer = sum_string_a
else : 
    answer = sum_string_b


# 더 해결 할 수 있는 부분이 있을까 ? 


print(answer)
