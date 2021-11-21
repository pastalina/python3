# Задание 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

arr = [random.randint(-99, 99) for _ in range(10)]
print(f'Исходный массив: {arr}')
min_id = 0
max_id = 0
for i in range(1, len(arr)):
    if arr[i] < arr[min_id]:
        min_id = i
    elif arr[i] > arr[max_id]:
        max_id = i
if min_id > max_id:
    min_id, max_id = max_id, min_id
summa = 0
for i in range(min_id + 1, max_id):
    summa += arr[i]
print(f'Сумма элементов между минимальным и максимальным элементами равна: {summa}')
