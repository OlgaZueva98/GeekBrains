# Задание 4.

def unique(numbers):
    unique_el = [el for el in numbers if numbers.count(el) == 1]

    return unique_el


print(f'Уникальные элементы списка: {unique( [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])}.')