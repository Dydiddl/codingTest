# 내가 생각한 첫번째 해결법
my_string = 'abcdevwxyz'
comparison_alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
answer = ''

for j in my_string:
    for i in comparison_alp:
        if i == j:
            my_string = my_string.replace(j, 'l')
        else:
            pass
print(my_string)
