# Задание 2.

def user_data(*args):
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    town = input('Введите город проживания: ')
    email = input('Введите email: ')
    phone = input('Введите телефон: ')
    data = ' '.join([name, surname, town, email, phone])
    return data

print(f'Пользовательские данные: {user_data()}.')
