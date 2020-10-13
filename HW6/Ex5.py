# Задание 5.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Ваш инструмент - {self.title}. Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Ваш инструмент - {self.title}. Запуск отрисовки карандашом.')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Ваш инструмент - {self.title}. Запуск отрисовки маркером.')


pen =  Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('мвркер')

pen.draw()
pencil.draw()
handle.draw()
