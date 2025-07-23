ineq = '>'
eq = '!'
n = 41
m = 78
answer = 0

new_eq = ineq + eq
if n >= m and new_eq == '>=':
    answer = "1, 1번작동"
elif n <= m and new_eq == '<=':
    answer = "1, 2번작동"
elif n > m and new_eq == '>!':
    answer = "1, 3번작동"
elif n < m and new_eq == '<!':
    answer = "1, 4번작동"
else: 
    answer = "0, 5번작동"
 
print(answer)
