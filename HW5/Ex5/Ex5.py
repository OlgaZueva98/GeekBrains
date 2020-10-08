# Задание 5.

import random


numbers = [n for n in range(0, 10)]
random.shuffle(numbers)

with open('numbers.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join([str(n) for n in numbers]))

with open('numbers.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    summa = sum([int(l) for l in lines])

print(f'Сумма чисел в файле: {summa}')
