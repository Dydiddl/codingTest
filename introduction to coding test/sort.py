# 중복 되는 것에 문제가 있음 수정
num = [7, 2, 3, 3, 5]

# list 길이 n개 짜리에서 가장 큰수는 자기보다 작은 숫자 갯수 n-1개
# 1:0, 2:1, 3:2, 4:3, 5:4
comparison_key = {} # 딕셔너리 정의 : 키값=
n = 0
count = 0
duplication = []
sort_num = []
for i in range(len(num)):
    while n < len(num):
        if num[i] == num[n]:
            count += 0
            n += 1
        elif num[i] > num[n]:
            count += 1
            n += 1
        else:
            count += 0
            n += 1
    if count in comparison_key:
        print("중복된 값이 있습니다. 중복된 값은{}입니다.".format(num[i]))
        duplication.append(num[i])
    comparison_key[count] = num[i]
    count = 0
    n = 0
    
print(comparison_key)

for i in num:
    if comparison_key[i] in duplication:
        sort_num.append(str(comparison_key[i] * duplication.count(i)))
    else:
        sort_num.append(str(comparison_key[i]))
print(sort_num)



# 딕셔너리 없이 해보기


