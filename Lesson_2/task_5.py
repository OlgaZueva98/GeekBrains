# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


s1 = 32
s2 = 127
i = 1
for char in range(s1, s2 + 1):
    if i % 10 == 0:
        print(f'{char}: {chr(char)}')
    else:
        print(f'{char}: {chr(char)}', end=' ')
    i += 1
