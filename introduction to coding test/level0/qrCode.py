q = 3
r = 1
code = 'qjnwezgrpirldywt'
qr_code = ''

for i in range(len(code)):
    if i % q == r:
        qr_code += code[i]

print(qr_code)

# code[r::q] -> 내가 쓴 코드와 같은 역할을 한다.
# 