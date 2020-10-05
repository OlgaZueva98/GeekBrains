# Задание 5.

from functools import reduce


def list_generator():
    result = reduce(lambda x,y: x * y, [n for n in range(100, 1001, 2)])

    return result


print(f'Чётные числа от 100 до 1000: {[n for n in range(100, 1001, 2)]}.'
      f'\nПроизведение всех элементов списка: {list_generator()}.')
