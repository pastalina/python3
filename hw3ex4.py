# Задание 4. Определить, какое число в массиве встречается чаще всего.

import random

arr = [random.randint(0, 100) for _ in range(10)]
print(f'Исходный массив: {arr}')
common_el = arr[0]
common_el_count = 1
for i in range(len(arr)-1):
    el_count = 1
    for k in range(i + 1, len(arr)):
        if arr[i] == arr[k]:
            el_count += 1
    if el_count > common_el_count:
        common_el_count = el_count
        common_el = arr[i]
if common_el_count > 1:
    print(f'Число {common_el} встречается {common_el_count} раз(а)')
else:
    print('Все элементы уникальны')
