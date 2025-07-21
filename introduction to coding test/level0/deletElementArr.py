arr = [1, 2, 3, 4, 5]
delete_list = [3, 6, 7, 8, 9]

# .index()를  사용해보자

# try:
#     print(arr.index(delete_list[2]))
# except:
#     pass
# try:
#     for i in range(len(delete_list)):
#         if arr.index(delete_list[i])
# except:
#     pass


# 기존 리스트를 사용해서 해결
for i in arr :
    for j in delete_list:
        if i == j :
            arr.remove(j)
        else:
            pass