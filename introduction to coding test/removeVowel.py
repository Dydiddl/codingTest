vowel = ['a', 'e', 'i', 'o', 'u']
my_string = "Nice to meet you"
new_string = ""


# for i in list(my_string):
#     for j in vowel:
#         if i == j:
#             my_string.replace(i, '')
# print(my_string)


print(my_string.replace('a', ''))
print(my_string.replace('e', ''))
print(my_string.replace('i', ''))
print(my_string.replace('o', ''))
print(my_string.replace('u', ''))

for i in vowel:
    my_string = my_string.replace(i, '')
    print(my_string)