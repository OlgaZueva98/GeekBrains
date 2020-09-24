##Задание 1.

a = 5
b = "пять"
print(str(a) + ' - ' + b)

year = int(input('Enter the year of birth: '))
age = int(input('Enter your age: '))
name = input('Enter your name: ')
surname = input('Enter your surname: ')
print(f'{name} {surname} was born in {year}, {age} years ago.')


##Задание 2.

time_in_sec = int(input('Enter time in seconds: '))
hours = time_in_sec // 3600
minutes = (time_in_sec - hours * 3600) // 60
seconds = time_in_sec - (hours * 3600 + minutes * 60)
print(f'Time is {hours}:{minutes}:{seconds}.')


##Задание 3.

n = int(input('Enter your number: '))
summa = n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n))
print(f'The sum is : {summa}.')


##Задание 4.

number = abs(int(input('Enter your number: ')))
#list_of_numerals = [int(n) for n in str(number)]
#max_number = max(list_of_numerals)
#print(max_number)
list_of_numerals = []
while number > 10:
    list_of_numerals.append(number % 10)
    number = number // 10
print(f'Max numeral is: {max(list_of_numerals)}.')


##Задание 5.

profit = float(input('Enter proceeds: '))
costs = float(input('Enter costs: '))
if profit > costs:
    print('Profit is greater than costs.')
    profitability = profit / costs
    print(f'Profitability is {profitability}.')
    workers = int(input('Enter number of workers: '))
    profit_per_worker = profit / workers
    print(f'Profit per worker is {profit_per_worker}.')
elif profit == costs:
    print('Profit and costs are equal.')
else:
    print('Profit is less than costs.')


##Задание 6.

a = int(input('Enter first day run result (km): '))
b = int(input('Enter expected result (km): '))
result = a
days = 1
while result < b:
    a = a + a * 0.1
    result += a
    days += 1
print(f'An athlete will get the expected results in {days} days.')