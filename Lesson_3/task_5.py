# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

from random import randint
import math


lst = [randint(-10, 10) for i in range(100)]
max_item = -math.inf

for idx, item in enumerate(lst):
    if 0 > item > max_item:
        max_item = item
        max_idx = idx

print(f'Максимальный отрицательный элемент массива: {max_item}. Позиция элемента: {max_idx}.')
