# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

lett1 = input('Введите букву латинского алфавита: ')
lett2 = input('Введите букву латинского алфавита: ')

lett1_pos = ord(lett1) - 96
lett2_pos = ord(lett2) - 96
dist = abs(lett1_pos - lett2_pos) - 1

print(f'Буква {lett1} занимает {lett1_pos}-е место.\n'
      f'Буква {lett2} занимает {lett2_pos}-е место.\n'
      f'Между буквами {lett1} и {lett2} находится {dist} букв.')