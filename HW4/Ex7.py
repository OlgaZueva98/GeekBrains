# Задание 7.

def fact(n):
    if n <= 1:
        yield 1
        return 1
    else:
        f = n * (yield from fact(n - 1))
        yield f
        return f


for el in fact(9):
    print(el)
