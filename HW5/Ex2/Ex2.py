# Задание 2.

words_count = {}
with open('Tochmarc Étaíne.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    lines_count = len(lines)
    for idx, l in enumerate(lines, start=1):
        words_count[idx] = len(l.split())

print(f'Количесвто строк в документе: {lines_count}' + '\n' + f'Количество слов в каждой сроке: {words_count}')

