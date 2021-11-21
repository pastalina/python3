# Задание 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

arr = [random.randint(0, 99) for _ in range(10)]
print(f'Исходный массив: {arr}')
max_el = arr[0]
min_el = arr[0]
for el in arr:
    if el > max_el:
        max_el = el
    elif el < min_el:
        min_el = el
min_el_index = arr.index(min_el)
max_el_index = arr.index(max_el)
arr[min_el_index], arr[max_el_index] = arr[max_el_index], arr[min_el_index]
print(f'Минимальный элемент - {min_el}, максимальный элемент - {max_el}.\nМассив после перестановки минимального и '
      f'максимального элементов: {arr}')
