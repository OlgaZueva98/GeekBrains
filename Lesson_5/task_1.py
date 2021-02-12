# 1. Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple


C = namedtuple('Company', ['name', 'profit', 'quarter'])
companies = []
profit_all = 0
quarters = 4

c_amount = int(input('Введите количество предприятий: '))
for i in range(1, c_amount+1):
    name = input(f'Введите название {i} предприятия: ')

    profits = []
    for j in range(1, quarters + 1):
        profit = float(input(f'Введите прибыль за {j} квартал: '))
        profits.append(profit)

    profit_all += sum(profits)

    company = C(name=name, profit=sum(profits), quarter=profits)

    companies.append(company)

profit_avg = profit_all / c_amount

more_avg = []
less_avg = []
for company in companies:
    if company.profit > profit_avg:
        more_avg.append(company)
    else:
        less_avg.append(company)

print(f'Средняя прибыль предприятий за год составила {profit_avg}.')

print('Предприятия с прибылью выше среднего:')
for company in more_avg:
    print(f'Прибыль {company.name} составила - {company.profit}.')

print('Предприятия с прибылью ниже среднего:')
for company in less_avg:
    print(f'Прибыль {company.name} составила - {company.profit}.')
