# Задание 7.

import json


profits = {}
all_profits = []
mean = {}

with open('firms.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for l in lines:
        name, ownership, income, costs = l.split()
        profit = int(income) - int(costs)
        profits[name] = profit
        if profit > 0:
            all_profits.append(profit)

average = sum(all_profits) // len(all_profits)
mean['average_profit'] = average
firms_data = [profits, mean]

print(firms_data)

with open('firms_data.json', 'w', encoding='utf-8') as f:
    json.dump(firms_data, f)
