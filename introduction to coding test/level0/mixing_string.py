str1 = 'aaa'
str2 = 'bbb'
# new_str = ''

# for 문 사용 해답
# for i in range(len(str1)):
#     new_str += str1[i] + str2[i]

# .join 함수 사용 해답, join은 리스트를 문자열로 바꾸는 것이기 때문에 리스트로 만드는 [] 가 포함되어있음
new_str = ''.join([str1[i] + str2[i] for i in range(len(str1))])

print(new_str)

