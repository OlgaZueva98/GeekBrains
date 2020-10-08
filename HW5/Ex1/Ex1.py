# Задание 1.

with open('my_file.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Введите строку: ')
        if line != '':
            f.write(line + '\n')
        else:
            break
