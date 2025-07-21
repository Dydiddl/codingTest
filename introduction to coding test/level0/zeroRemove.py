n_str = '0010'
answer = ''
for i in range(len(n_str)):
    if n_str[i] =='0':
        new_str = n_str[i+1:]
    else:
        break
if not answer:
    answer = n_str
print(new_str)
