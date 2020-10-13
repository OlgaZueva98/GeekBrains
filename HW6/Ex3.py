# Задание 3.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


pos = Position('Ivan', 'Ivanov', 'full-stack developer', 100000, 5000)
print(f'Полное имя сотрудника: {pos.get_full_name()}.' + '\n' +
      f'Доход с учётом премии: {pos.get_total_income()}.')
