# Задание 4.

# Решение с помощью оператора:
def my_func(x, y):
    result = x ** y

    return result

x = int(input('Введите действительное положительное число: '))
y = int(input('Введите дцелое отрицательное число: '))
print(f'Сумма: {my_func(x, y)}.')

# Решение с помощью цикла:
def my_func(x, y):
    result = x
    for i in range(abs(y) - 1):
        result = result * x

    return 1 / result

x = int(input('Введите действительное положительное число: '))
y = int(input('Введите дцелое отрицательное число: '))
print(f'Сумма: {my_func(x, y)}.')