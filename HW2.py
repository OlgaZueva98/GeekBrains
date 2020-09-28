# Задание 1.

my_list = [5, 'python', False, 5.5, None]
for el in my_list:
    print(f'Элемент {el} относится к типу {type(el)}.')


# Задание 2.

length = int(input('Введите желаемую длину списка: '))
my_list = [el for el in range(0, length)]
for el in range(1, length, 2):
    my_list[el], my_list[el - 1] = my_list[el - 1], my_list[el]
print(my_list)


# Задание 3.

# Решение через list:
month = int(input('Введите порядковый номер месяца: '))
seasons = ['зима', 'весна', 'лето', 'осень']
if month in [12, 1, 2]:
    print(f'Этот месяц относится к {seasons[0][:-1]}' + 'е.')
elif month in [3, 4, 5]:
    print(f'Этот месяц относится к {seasons[1][:-1]}' + 'е.')
elif month in [6, 7, 8]:
    print(f'Этот месяц относится к {seasons[2][:-1]}' + 'у.')
elif month in [9, 10, 11]:
    print(f'Этот месяц относится к {seasons[3][:-1]}' + 'и.')
else:
    print('Ошибка! Введите число от 1 до 12.')

# Решение через dict:
month = int(input('Введите порядковый номер месяца: '))
seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for key, value in seasons.items():
    if month in value:
        print(f'Время года - {key}.')


# Задание 4.

sent = input('Введите предложение: ')
words = sent.split()
for idx, w in enumerate(words, start=1):
    if len(w) <= 10:
        print(str(idx) + ' ' + w)
    else:
        print(str(idx) + ' ' + w[:10])


# Задание 5.

length = int(input('Введите желаемую длину списка: '))
my_list = [el for el in range(0, length)]
my_list.sort(reverse=True)
print('Текущий рейтинг: ' + str(my_list))

new_el = int(input('Введите новый элемент списка: '))
if new_el > max(my_list):
    my_list.insert(0, new_el)
elif new_el in my_list:
    my_list.insert(my_list.index(new_el), new_el)
else:
    my_list.append(new_el)

print('Обновлённый рейтинг: ' + str(my_list))


# Задание 6.

products = []
params = []
params_str = input('Введите характеристики товара в формате - название, цена, количество, единица измерения; ... : ')
for par in params_str.split(';'):
    params.append(par.split(', '))

i = 0
for l in params:
    i += 1
    info = {'название': l[0], 'цена': int(l[1]), 'количество': int(l[2]), 'ед': l[3]}
    products.append(tuple((i, info)))

print('Структура "Товары": ' + '\n' + str(products))

names = []
cost = []
amount = []
unit = []
for prod in products:
    names.append(prod[1]['название'])
    cost.append(prod[1]['цена'])
    amount.append(prod[1]['количество'])
    unit.append(prod[1]['ед'])

data = {'название': names, 'цена': cost, 'количество': amount, 'ед': unit}
print('Аналитика: ' + '\n' + str(data))
