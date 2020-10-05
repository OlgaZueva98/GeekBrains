# Задание 2.

def greater_than(numbers):
    great_num = [numbers[i] for i in range(1, len(numbers)) if numbers[i - 1] < numbers[i]]

    return great_num


print(f'Элементы исходного списка, значения которых больше предыдущего: '
      f'{greater_than([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])}.')
