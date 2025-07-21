dot = [2, 4]
position = 0

if dot[0] > 0 :
    if dot[1] > 0:
        position += 1
    else:
        position += 4
else:
    if dot [1] > 0:
        position += 2
    else:
        position += 3

print(position)