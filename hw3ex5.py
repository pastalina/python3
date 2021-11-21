# Задание 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

arr = [random.randint(-99, 99) for _ in range(10)]
print(f'Исходный массив: {arr}')
i = 0
index = -1
while i < len(arr):
    if arr[i] < 0:
        if index == -1:
            index = i
        elif arr[i] > arr[index]:
            index = i
    i += 1
print(f'Максимальный отрицательный элемент массива: {arr[index]}. Его индекс: {index+1}')
