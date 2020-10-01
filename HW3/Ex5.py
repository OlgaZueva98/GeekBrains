# Задание 5.

def summ():
    summa = 0
    while True:
        try:
            user_input = input('Введите числа через пробел: ')
            numbers = user_input.split()
            for el in numbers:
                summa += int(el)
            print(summa)
        except ValueError:
            print(summa)
            print("Value Error")
            break

summ()