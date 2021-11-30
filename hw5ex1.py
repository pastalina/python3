# Задание 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для
# каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple
from statistics import mean

New_Company = namedtuple('New_Company', 'name profit_list avg')

lst = []
for i in range(int(input('Введите количество компаний: '))):
    arg = input('Введите в строку имя и поквартальную прибыль компании через пробел:\n').split()
    lst.append(New_Company(arg[0], arg[1:], mean(map(int, arg[1:5]))))

avg = mean([i.avg for i in lst])

for i in lst:
    print(f'Компания: {i.name}\t\t\tСредняя прибыль за год: {i.avg}')

print('*' * 70)
print(f'Средняя годовая прибыль среди всех компаний: {avg}')
print('Компании с прибылью меньше средней: ')
for i in lst:
    if i.avg < avg:
        print(i.name)

print('Компании с прибылью больше средней: ')
for i in lst:
    if i.avg > avg:
        print(i.name)
