# 1) Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.

# 4. Определить, какое число в массиве встречается чаще всего.
import timeit
import cProfile

# Вариант 1.
from collections import Counter
from random import randint


def count_max_1(size):
    lst = [randint(0, 100) for i in range(size)]
    c = Counter(lst)
    return c.most_common()[0][0]

# Вариант 2.


def count_max_2(size):
    lst = [randint(0, 100) for i in range(size)]
    freq_dict = {}
    num = lst[0]
    max_freq = 1

    for n in lst:
        if n in freq_dict:
            freq_dict[n] += 1
        else:
            freq_dict[n] = 1

        if freq_dict[n] > max_freq:
            num = n
            max_freq = freq_dict[n]

    if max_freq > 1:
        return num

# Вариант 3.


def count_max_3(size):
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

    if max_freq > 1:
        return num


print(timeit.timeit('count_max_1(100)', number=1000, globals=globals())) #0.19238270000000002
print(cProfile.run('count_max_1(100)'))
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.012    0.012 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 __init__.py:550(__init__)
#        1    0.000    0.000    0.000    0.000 __init__.py:575(most_common)
#        1    0.000    0.000    0.000    0.000 __init__.py:619(update)
#        1    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
#      100    0.000    0.000    0.012    0.000 random.py:174(randrange)
#      100    0.000    0.000    0.012    0.000 random.py:218(randint)
#      100    0.012    0.000    0.012    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.012    0.012 scratch.py:11(count_max_1)
#        1    0.000    0.000    0.012    0.012 scratch.py:12(<listcomp>)
#        1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
#        1    0.000    0.000    0.000    0.000 {built-in method _collections._count_elements}
#        1    0.000    0.000    0.012    0.012 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
#      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      118    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

print(timeit.timeit('count_max_2(100)', number=1000, globals=globals())) #0.18159159999999996
print(cProfile.run('count_max_2(100)'))
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#      100    0.000    0.000    0.000    0.000 random.py:218(randint)
#      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.000    0.000 scratch.py:17(count_max_2)
#        1    0.000    0.000    0.000    0.000 scratch.py:18(<listcomp>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      135    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

print(timeit.timeit('count_max_3(100)', number=1000, globals=globals())) #0.6439537
print(cProfile.run('count_max_3(100)'))
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
#      100    0.000    0.000    0.000    0.000 random.py:218(randint)
#      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.001    0.001 scratch.py:37(count_max_3)
#        1    0.000    0.000    0.000    0.000 scratch.py:38(<listcomp>)
#        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       57    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      132    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


#Вариант 2 оказался быстрее.
