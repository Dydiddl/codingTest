# n = 3

# arrangement = []
# make_list = []

# for i in range(n):
#     for j in range(n):
#         if i == j :
#             make_list.append(1)
#         else: 
#             make_list.append(0)
#     arrangement.append(make_list)
#     del (make_list[:])
# print(arrangement)

n = 4
arrangement_string = ''
for i in range(n):
    for j in range(n):
        if i == j:
            arrangement_string += '1'
        else:
            arrangement_string += '0'
    arrangement_string += ' '

arrangement_string_strip = arrangement_string.rstrip()
arrangement_list = arrangement_string_strip.split(' ')

for i in range(n):
    arrangement_list[i] = list(map(int,arrangement_list[i]))
        

print(arrangement_list)

print(arrangement_list[0][0])



# 0:n-1,n,n+1:2n-1,2n,


# s = ''
# s += '1'
# s += '0'
# s += '1'
# s += '0'


# make_list = []

# print(s)
# print(type(s))

# for i in range(len(s)):
#     make_list.append(int(s[i]))

# print(make_list)

