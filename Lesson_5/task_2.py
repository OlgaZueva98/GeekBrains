# 2. Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.


from collections import deque


hex_1 = list(input('Введите первое шестнадцатиричное число: '))
hex_2 = list(input('Введите второе шестнадцатиричное число: '))
numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15}
inv_numbers = {value: key for key, value in numbers.items()}


def sum_hex(hex_1, hex_2):
    hex_1 = hex_1[::-1]
    hex_2 = hex_2[::-1]

    if len(hex_1) > len(hex_2):
        maxHex = hex_1
        minHex = hex_2
    else:
        maxHex = hex_2
        minHex = hex_1

    sum = deque()

    add = 0
    for i in range(len(maxHex)):
        first = numbers[maxHex[i]]
        try:
            second = numbers[minHex[i]]
        except IndexError:
            second = 0

        temp = first + second + add

        if temp > 15:
            add = 1
            temp -= 16
        else:
            add = 0

        sum.appendleft(inv_numbers[temp])

    if add != 0:
        sum.appendleft(add)

    return sum


def mul_hex(hex_1, hex_2):
    hex_1 = hex_1[::-1]
    hex_2 = hex_2[::-1]

    if len(hex_1) > len(hex_2):
        maxHex = hex_1
        minHex = hex_2
    else:
        maxHex = hex_2
        minHex = hex_1

    mul = deque()

    for i in range(len(minHex)):
        add = 0
        for j in range(len(maxHex)):
            temp = numbers[minHex[i]] * numbers[maxHex[j]] + add
            if temp > 15:
                add = temp // 16
                temp %= 16
            else:
                add = 0

            mul.appendleft(inv_numbers[temp])

        if add != 0:
            mul.appendleft(add)

    return mul


print(sum_hex(hex_1, hex_2))
print(mul_hex(hex_1, hex_2))
