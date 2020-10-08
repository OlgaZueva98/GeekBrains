# Задание 3.

workers = {}
with open('workers.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    workers_count = len(lines)
    for l in lines:
        name, salary = l.split()
        workers[name] = int(salary)

less_salary = [k for k in workers.keys() if workers[k] < 20000]
mean_sal = sum(workers.values()) / workers_count

print(f'Сотрудники с окладом менее 20 тыс.: {", ".join(less_salary)}.' + '\n' + f'Средняя величина дохода: {mean_sal}.')
