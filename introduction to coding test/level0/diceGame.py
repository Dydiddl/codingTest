a = 3
b = 5
a_judgment = a % 2
b_judgment = b % 2
score = 0

if a_judgment == 1 and b_judgment ==1:
    score += a ** 2 + b **2
elif a_judgment ==1 or b_judgment ==1:
    score += 2 * (a + b)
else:
    if a > b:
        score += a - b
    else:
        score += b - a
print(score)