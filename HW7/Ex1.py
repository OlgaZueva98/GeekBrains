# Задание 1.

class Matrix:

    def __init__(self, list_1, list_2):
        self.matr_1 = list_1
        self.matr_2 = list_2

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matr_1)

    def __add__(self):
        summa = []
        result = []

        for i in range(len(self.matr_1)):
            for j in range(len(self.matr_1[0])):
                matr_sum = self.matr_2[i][j] + self.matr_1[i][j]
                summa.append(matr_sum)
                if len(summa) == len(self.matr_1):
                    result.append(summa)
                    summa = []

        return '\n'.join('\t'.join(map(str, row)) for row in result)


matrix = Matrix([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]],
                [[5, 2, 3],
                [8, 5, 7],
                [2, 1, 0]])

print(f'Матрица:\n{matrix.__str__()}')
print(f'Сумма двух матриц:\n{matrix.__add__()}')
