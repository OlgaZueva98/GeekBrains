# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы


from random import randint


SIZE = 100


def bubble_sort(arr):
    n = 1
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1

    return arr


arr = [randint(-100, 99) for i in range(SIZE)]
print(f'Исходный массив: {arr}')
print(f'Отсортированный массив: {bubble_sort(arr)}')
