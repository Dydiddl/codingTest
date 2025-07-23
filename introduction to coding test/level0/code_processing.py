code = 'abc1abc1abc'
print(len(code))


# 모드는 0부터 시작, code의 '1'이 나오면 모드 1로 바뀜, 다시 바뀌면 0으로 바뀜, 반복
# 클래스를 만들어보자
# class codeMode:
#     def code_mode(self=str):
#         self.mode_num = 0
#         result = ''
#         for i in range(len(self)):
#             if self.mode_num == 0:
#                 if self[i] != '1':
#                     if i % 2 == 0:
#                         result += self[i]
#                 else:
#                     self.mode_num += 1
#             if self.mode_num != 0:
#                 if self[i] != '1':
#                     if i % 2 != 0:
#                         result += self[i]
#                 else:
#                     self.mode_num -= 1
#         return result

# code.code_mode()


# 클래스 없이
mode_num = 0
result = ''
for i in range(len(code)):
    if mode_num == 0:
        if code[i] != '1':
            if i % 2 == 0:
                result += code[i]
                mode_num = 0
            else:
                mode_num = 0
                pass
        else:
            mode_num = 1
    elif mode_num == 1:
        if code[i] != '1':
            if i % 2 != 0:
                result += code[i]
                mode_num = 1
            else:
                mode_num = 1
                pass
        else:
            mode_num = 0
if result == '':
    result += 'EMPTY'
print(result)


# mode ^= 1 
# ^= 는 비트연산자 중에 xor을 뜻합니다. 두 비트가 서로 같으면 0 다르면 1입니다. 따라서 mode가 0이면 결과는 1이되고, 1이면 같기때문에 0이됩니다.

