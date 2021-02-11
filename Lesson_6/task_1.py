# 1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# ОС: 64bit
# Python: 3.7.6


from sys import getsizeof
from random import randint
import math


def memory(vars):
    mem_sum = 0
    values = []

    for k, v in vars.items():
        if not k.startswith('__'):
            if v not in values:
                values.append(v)
                mem_sum += getsizeof(v)

    return mem_sum


# 5. В массиве найти максимальный отрицательный элемент.

def max_neg(size):
    lst = [randint(-10, 10) for i in range(size)]
    max_item = -math.inf

    for idx, item in enumerate(lst):
        if 0 > item > max_item:
            max_item = item
            max_idx = idx

    print(memory(locals()))

    return max_item, max_idx

# 1052 байт


# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

def max_min(size):
    lst = [randint(-10, 100) for i in range(size)]
    idx_min = 0
    idx_max = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[idx_max]:
            idx_max = i
        if lst[i] < lst[idx_min]:
            idx_min = i
    lst[idx_min], lst[idx_max] = lst[idx_max], lst[idx_min]

    print(memory(locals()))

    return lst

# 1024 байт


# 4. Определить, какое число в массиве встречается чаще всего.

def count_max(size):
    lst = [randint(0, 100) for i in range(size)]
    max_freq = 1
    num = lst[0]
    unique = set(lst)

    for n in unique:
        freq = 0
        for i in range(len(lst)):
            if n == lst[i]:
                freq += 1
        if freq > max_freq:
            max_freq = freq
            num = n

    print(memory(locals()))

    if max_freq > 1:
        return num

# 3324 байт


print(max_neg(100))
print(max_min(100))
print(count_max(100))
