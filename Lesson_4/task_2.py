# 2) Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.

import timeit
import cProfile

# 2.1. С помощью алгоритма «Решето Эратосфена»


def sieve(n):
    lst = [i for i in range(n + 1)]
    lst[1] = 0
    i = 2

    while i <= n:
        if lst[i] != 0:
            j = i * 2
            while j <= n:
                lst[j] = 0
                j = j + i
        i += 1

    prime = [i for i in lst if i != 0]

    return prime[-1]


print(sieve(20))

# 2.2. Без использования «Решета Эратосфена».
import math


def prime(n):
    lst = [i for i in range(n + 1)]
    lst = set(lst)
    lst.remove(0)

    for i in range(2, int(math.sqrt(n))):
        if i in lst:
            set.difference_update(lst, set(range(2 * i, n+1, i)))

    lst = list(lst)

    return lst[-1]


print(prime(20))


print(timeit.timeit('sieve(20)', number=1000, globals=globals())) #0.017326400000000006
print(cProfile.run('sieve(20)'))
#6 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_2.py:10(sieve)
#        1    0.000    0.000    0.000    0.000 task_2.py:11(<listcomp>)
#        1    0.000    0.000    0.000    0.000 task_2.py:23(<listcomp>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#Сложность = O(n^2)


print(timeit.timeit('prime(20)', number=1000, globals=globals())) #0.014639199999999991
print(cProfile.run('prime(20)'))
#9 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 task_2.py:34(prime)
#        1    0.000    0.000    0.000    0.000 task_2.py:35(<listcomp>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#        2    0.000    0.000    0.000    0.000 {method 'difference_update' of 'set' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        1    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}

#Сложность = O(n)
