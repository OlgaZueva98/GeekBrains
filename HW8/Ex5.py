# Задание 4.

class ComplexNumber:
    def __init__(self, a, b):
        self.z = complex(a, b)

    def __add__(self, other1, other2):
        other = ComplexNumber(other1, other2)
        return f'Результат сложения: {self.z + other.z}'

    def __mul__(self, other1, other2):
        other = ComplexNumber(other1, other2)
        return f'Результат умножения: {self.z * other.z}'


z = ComplexNumber(2, 3)
print(z.__add__(1, 2))
print(z.__mul__(2, 1))
