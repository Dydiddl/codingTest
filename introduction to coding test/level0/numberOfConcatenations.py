num_list = [3, 4, 5, 2, 1]

even_num = ''.join(str(num) for num in num_list if num % 2 == 0)
odd_num = ''.join(str(num) for num in num_list if num % 2 != 0)