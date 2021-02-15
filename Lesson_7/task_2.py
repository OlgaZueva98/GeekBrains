# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


from random import randint


SIZE = 100


def merge(left, right):
    sorted_list = []
    left_idx = 0
    right_idx = 0

    length = len(left) + len(right)

    for _ in range(length):
        if left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                sorted_list.append(left[left_idx])
                left_idx += 1
            else:
                sorted_list.append(right[right_idx])
                right_idx += 1
        elif left_idx == len(left):
            sorted_list.append(right[right_idx])
            right_idx += 1
        elif right_idx == len(right):
            sorted_list.append(left[left_idx])
            left_idx += 1

    return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    else:
        middle = len(arr) // 2

        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])

        return merge(left, right)


arr = [randint(0, 49) for i in range(SIZE)]
print(f'Исходный массив: {arr}')
print(f'Отсортированный массив: {merge_sort(arr)}')
