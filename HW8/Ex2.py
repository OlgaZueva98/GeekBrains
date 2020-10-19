# Задание 2.

class Division_by_Zero:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def div(dividend, divider):
        try:
            return dividend / divider
        except:
            return f'{divider}\nZeroDivisionError: division by zero'


print(Division_by_Zero.div(50, 0))
print()
d = Division_by_Zero(50, 25)
print(d.div(50, 25))
