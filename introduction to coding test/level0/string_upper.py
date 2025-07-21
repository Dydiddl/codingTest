a = 'abAcDef'
new_a = ''

# # a.lower() for전에 실행 후 코드 작성
# a = a.lower()
# for i in range(len(a)):
#     if a[i] == 'a':
#         new_a += a[i].upper()
#     else:
#         new_a += a[i].lower()
# print(new_a)


# # a.lower() 안쓰고 하는 for 코드 작성
# for i in range(len(a)):
#     if a[i].isupper() == True:
#         if a[i] == 'A':
#             new_a += a[i]
#         else:
#             new_a += a[i].lower()
#     else:
#         if a[i] == 'a':
#             new_a += a[i].upper()
#         else:
#             new_a += a[i]
# print(new_a)


# 준우 피드백 받고 작성
for i in range(len(a)):
    if a[i] == 'a' or a[i] == 'A':
        new_a += a[i].upper()
    else:
        new_a += a[i].lower()
print(new_a)