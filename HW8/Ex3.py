# Задание 3.

class IfNumber:
    def __init__(self, number, list_):
        self.number = number
        self.list_ = list_

    def check(self):
        try:
            self.list_.append(int(self.number))
            print(f'Current list: {self.list_}')
        except:
            print(f'{self.number} is not a number!\nTry again.')


list_ = []

while True:
    number = input('Введите число: ')
    if number.lower() != 'stop':
        n = IfNumber(number, list_)
        n.check()
    else:
        print(list_)
        break
