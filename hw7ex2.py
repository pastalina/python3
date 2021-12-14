# Задание 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

size = 10
array = [round(random.uniform(0, 50), 3) for i in range(size)]
print('Исходный массив:\n', array)


def merge_sort(array):

    def merge_list(a, b):
        c = []
        n = len(a)
        m = len(b)

        i = 0
        j = 0
        while i < n and j < m:
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1

        c += a[i:] + b[j:]
        return c

    n1 = len(array) // 2
    a1 = array[:n1]
    a2 = array[n1:]

    if len(a1) > 1:
        a1 = merge_sort(a1)
    if len(a2) > 1:
        a2 = merge_sort(a2)

    return merge_list(a1, a2)


print('Отсортированный по возрастанию методом слияния массив:\n', merge_sort(array))
