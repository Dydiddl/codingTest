sides = [1,2,3]
maxNum = max(sides)
sides.remove(max(sides))
remainNumSum = sum(sides)

if maxNum < remainNumSum:
    result = 2



print(maxNum)
print(sides)
print(remainNumSum)