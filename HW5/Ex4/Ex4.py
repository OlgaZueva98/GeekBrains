# Задание 4.

numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('eng_numbers.txt', 'r', encoding='utf-8') as f:
    eng = f.readlines()

with open('rus_numbers.txt', 'w', encoding='utf-8') as f:
    for l in eng:
        eng_num = l.split()[0]
        for k in numbers.keys():
            if k == eng_num:
                f.write(l.replace(eng_num, numbers[k]))
