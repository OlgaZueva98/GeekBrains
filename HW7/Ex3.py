# Задание 3.

class Cell:

    def __init__(self, amount):
        self.amount = round(amount)

    def __str__(self):
        return "*" * self.amount

    def __add__(self, other):
        other = Cell(other)
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        other = Cell(other)
        diff = Cell(self.amount - other.amount)
        if self.amount - other.amount > 0:
            return diff
        else:
            print('Произвести вычитание невозможно.')

    def __mul__(self, other):
        other = Cell(other)
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        other = Cell(other)
        return Cell(self.amount / other.amount)

    def make_order(self, row):
        string = '*' * self.amount
        return '\\n'.join([string[s:s + row] for s in range(0, len(string), row)])


cell = Cell(12)
print(f'Результат сложения: {cell.__add__(10)}')
print(f'Результат вычитания: {cell.__sub__(10)}')
print(f'Результат умножения: {cell.__mul__(10)}')
print(f'Результат деления: {cell.__truediv__(10)}')
print(f'Ряды ячеек: {cell.make_order(5)}')
