arr = [0, 1, 2, 3, 4]
queries = [[0, 3], [1, 2], [1, 4]]
firstChnge = ''
secondChange = ''

# for i in queries:
#     firstChnge = arr[i[0]]
#     secondChange = arr[i[1]]
#     arr[i[0]] = secondChange
#     arr[i[1]] = firstChnge

# print(arr)

# 한번에 바꿔도 이전값들이 밀리는 현상이 없다. 

for i,j in queries:
    arr[i], arr[j] = arr[j], arr[i]

print(arr)


# for i in queries:
#     arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]

# print(arr)
