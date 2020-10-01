# Задание 3.

def my_func(*args):
    args = []
    a = args.append(int(input('Введите первое число: ')))
    b = args.append(int(input('Введите второе число: ')))
    c = args.append(int(input('Введите третье число: ')))
    args.sort()
    summa = args[1] + args[2]

    return summa

print(f'Сумма: {my_func()}.')
