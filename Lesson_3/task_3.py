# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint


lst = [randint(-10, 100) for i in range(100)]
idx_min = 0
idx_max = 0
for i in range(1, len(lst)):
    if lst[i] > lst[idx_max]:
        idx_max = i
    if lst[i] < lst[idx_min]:
        idx_min = i
lst[idx_min], lst[idx_max] = lst[idx_max], lst[idx_min]

print(', '.join([str(i) for i in lst]))
