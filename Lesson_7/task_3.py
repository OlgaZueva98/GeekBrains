# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.


import random


# Вариант 1

def find_median_1(m):
    arr = [random.randint(-100, 100) for _ in range(2 * m + 1)]
    sorted_arr = sorted(arr)

    print(f'Исходный массив: {arr}')
    return sorted_arr[m]


# Вариант 2

def quickselect(arr, k, pivot_fn):
    if len(arr) == 1:
        k == 0
        return arr[0]

    pivot = pivot_fn(arr)

    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


def find_median_2(m, pivot_fn=random.choice):
    arr = [random.randint(-100, 100) for i in range(2*m + 1)]
    print(f'Исходный массив: {arr}')

    if len(arr) % 2 == 1:
        return quickselect(arr, len(arr) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(arr, len(arr) / 2 - 1, pivot_fn) +
                      quickselect(arr, len(arr) / 2, pivot_fn))


print(f'Медиана массива: {find_median_1(10)}')
print(f'Медиана массива: {find_median_2(10)}')
