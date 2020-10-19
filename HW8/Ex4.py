# Задание 4.

import pandas as pd


class Warehouse:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        self.equip_war = {}

    def result(self):
        v1 = []
        v2 = []
        l = list(self.equip_war.values())
        for i in range(len(l)):
            v1.append(l[i][0])
            v2.append(l[i][1])

        return pd.DataFrame({"Наименование": self.equip_war.keys(), "Цена": v1, "Количество": v2})

class OfficeEquipment(Warehouse):
    def __init__(self, name, price, amount):
        super().__init__(name, price, amount)

    def check(self, equip):
        try:
            equip[self.name] = [int(self.price), int(self.amount)]
            print(f'Список товаров, доставленных на склад: {equip}')
        except:
            print('Недопустимый тип данных.')

    def receipt(self):
        equip = {}
        while True:
            n = input('Введите наименование: ')
            if n.lower() != 'stop':
                p = input('Введите цену: ')
                a = input('Введите количество: ')
                c = OfficeEquipment(n, p, a)
                c.check(equip)
            else:
                print(f'Список товаров: {equip}')
                break

        return self.equip_war.update(equip)

    def available(self):
        if self.name in self.equip_war.keys():
            for k in self.equip_war.keys():
                if self.name == k:
                    print(f'Товар {k} в наличии на складе в количестве {self.equip_war[k][1]} шт. Цена {self.equip_war[k][0]}.')
        else:
            print('Этого товара нет на складе.')

class Printer(OfficeEquipment):
    def __init__(self, name, price, amount):
        super().__init__(name, price, amount)
        self.types_p = ['струйные', 'лазерные']

    def __str__(self):
        return f'Принтер фирмы {self.name}.'

    @property
    def types(self):
        return f'Виды принтеров на складе: {", ".join(self.types_p)}'

class Scanner(OfficeEquipment):
    def __init__(self, name, price, amount):
        super().__init__(name, price, amount)
        self.types_s = ['планшетные', 'потоковые']

    def __str__(self):
        return f'Сканер фирмы {self.name}.'

    @property
    def types(self):
        return f'Виды сканеров на складе: {", ".join(self.types_s)}'

class Copier(OfficeEquipment):
    def __init__(self, name, price, amount):
        super().__init__(name, price, amount)
        self.types_c = ['аналоговые', 'цифровые']

    def __str__(self):
        return f'Ксерокс фирмы {self.name}.'

    @property
    def types(self):
        return f'Виды ксероксов на складе: {", ".join(self.types_c)}'


printer = Printer('Samsung', 20000, 10)
print(printer)
print(printer.types)
printer.receipt()
print()
print(printer.result())
printer.available()

scanner = Scanner('Canon', 17000, 15)
print(scanner)
print(scanner.types)
scanner.receipt()
print()
print(scanner.result())
scanner.available()

copier = Copier('Xerox', 10000, 12)
print(copier)
print(copier.types)
copier.receipt()
print()
print(copier.result())
copier.available()
