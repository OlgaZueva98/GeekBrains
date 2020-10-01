# Задание 1.

def division(*args):
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b != 0:
        return a / b
    else:
        return 'Error!'

print(f'Результат деления: {division()}.')
