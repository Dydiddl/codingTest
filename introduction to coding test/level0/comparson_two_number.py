a = 12
b = 3


# # 가장 먼저 떠오른 해답
# if int(str(a) + str (b)) > int(str(b) + str (a)):
#     answer = int(str(a) + str (b))
# else : 
#     answer = int(str(b) + str (a))


# # 중복되는 것을 해결 해보자
# # 이렇게 하면 a + b, b + a 를 최초에 한번만 계산하면 됨
# # 위의 해답은 총 3번의 계산이 이루어짐
# sum_string =int(str(a) + str(b))
# mul_int = 2 * a * b
# if sum_string >= mul_int:
#     answer = sum_string
# else : 
#     answer = mul_int


# 더 해결 할 수 있는 부분이 있을까 ? 

answer = max(int(str(a) + str(b)), 2 * a * b)


print(answer)
