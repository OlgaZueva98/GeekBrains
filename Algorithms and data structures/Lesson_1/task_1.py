# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = int(input('Введите трхзначное число: '))
nums = str(n)
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])

sum = a + b + c
comp = a * b * c

print(f'Сумма цифр трёхзначного числа: {sum}, \n'
      f'Произведение цифр трёхзначного числа: {comp}')