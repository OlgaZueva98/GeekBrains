# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.


import hashlib


def func(s):
    length = len(s)
    subs = set()

    for i in range(length):
        for j in range(length + i):
            h_subs = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            subs.add(h_subs)

    subs_num = len(subs) - 1

    return subs_num


print(f'Количество подстрок: {func("papa")}') #6
print(f'Количество подстрок: {func("sova")}') #9
