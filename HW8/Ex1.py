# Задание 1.

class Data:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'Текущая дата: {Data.transform(self.data)}'

    @classmethod
    def transform(cls, data):
        day, month, year = data.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def validation(data):
        calendar = {1: [31], 2: [28, 29], 3: [31], 4: [30], 5: [31],
                    6: [30], 7: [31], 8: [31], 9: [30], 10: [31],
                    11: [30], 12: [31]}
        day_month = {}

        day, month, year = Data.transform(data)
        day_month[month] = [day]

        if day_month.items() <= calendar.items():
            return 'Всё верно.'
        else:
            return 'Такой даты нет.'


print(Data.validation('31-10-2020'))
print(Data.transform('31-10-2020'))
print()
d = Data('31-10-2020')
print(d)
print(d.validation('35-10-2020'))
print(d.transform('32-10-2020'))
