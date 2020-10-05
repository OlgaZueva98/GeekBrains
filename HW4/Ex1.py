# Задание 1.

def salary(*args):
    hours = int(input('Введите выработку в часах: '))
    rate = int(input('Введите ставку в час: '))
    prem = int(input('Введите премию: '))
    salary = (hours * rate) + prem
    return salary


print(f'Заработная плата составит: {salary()}.')
