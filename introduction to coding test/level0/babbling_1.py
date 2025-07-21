babbling = ["aya", "yee", "u", "maa", "wyeoo"]
pronunciation = ['aya', 'ye', 'woo', 'ma']
count = 0
string_len = 0

for i in babbling:
    for j in pronunciation:
        string_len += len(i)
        while len(i) <= 1:
            