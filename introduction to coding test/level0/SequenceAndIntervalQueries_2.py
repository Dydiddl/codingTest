arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2], [0, 3, 2], [0, 2, 2]]

for i in queries:
    print(i)
    print(range(i[0], i[1] + 1))
    for j in range((i[0], i[1] + 1)):w
    #     print(arr[j])

# arr_list = []
# result = []
# arr = arr.sort()
# for i in queries:
#     for j in range(i[0], i[1]+1):
#         if arr[j] > i[2]:
#             result.append(arr[i])

# print(result)



# for j in queries:
#     for i in arr:
#         if i >= j[0] :
#             if i <= j[1]:
#                 if i > j[2] :
#                     arr_list.append(i)
#                 else:
#                     pass
#             else:
#                 pass
#         else:
#             pass
#     print(arr_list)
#     if len(arr_list) == 0:
#         result.append(-1)
#     else:
#         result.append(min(arr_list))
#         for x in arr_list:
#             arr_list.remove(x)
#             print(arr_list)

# print(result)