# Задание 6.a.

from itertools import count, cycle


def integers(a):
    for i in count(a):
        print(i)
        if i > 10:
            break


integers(3)


# Задание 6.b.

def repeat(l):
    c = 0
    for i in cycle(l):
        c += 1
        print(i)
        if c >= len(l) * 3:
            break


repeat([1, 2, 3, 4])
