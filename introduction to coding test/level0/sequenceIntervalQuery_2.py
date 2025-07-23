arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2], [0, 3, 2], [0, 2, 2]]

findMinimum = []
comparisonNumList = []


# 각 쿼리마다 순서대로 [s, e, k]
# s(queries[i][1]) <= i <= e(queries[i][1]) 인 모든 i
# i > k(queries[i][2]) and 가장작은 arr[i]를 찾는다.
# 단 특정 쿼리의 답이 존재하지 않으면 -1 출력

# queries 인덱스 
for i in queries:
    print("queries의 {} 값 에 대한 arr 값 : {}".format(i,arr[i[0]:i[1] + 1]))
# s, e, k 에 대한 arr 값의 비교작업, s, e 값에 따른 분류
    for j in arr[i[0]:i[1] + 1]:
        print("k값 {}과 비교할 arr 값 : {}".format(i[2],j))
# arr 분류작업, k 값에 따른 분류, k 보다 큰 값을 comparisonNumList에 추가하여, findMinimum에 2차 배열로 추가
        if j > i[2]:
            comparisonNumList.append(j)
    print(comparisonNumList)
    findMinimum.append(comparisonNumList)
                
print(findMinimum)

                
    # if arr[i[0]:] 
    # else:
    #     result = -1
    
