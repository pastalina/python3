# Задание 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве
# медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не
# меньше медианы, в другой — не больше медианы.
import random

n = 10
array = [random.randint(-100, 100) for i in range(2 * n + 1)]
print('Исходный массив:\n', array)


def median(array, k):
    if len(array) == 1:
        return array[0]

    pivot = random.choice(array)

    left_el = [el for el in array if el < pivot]
    right_el = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(left_el):
        return median(left_el, k)
    elif k < len(left_el) + len(pivots):
        return pivots[0]
    else:
        return median(right_el, k - len(left_el) - len(pivots))


print('Медиана для данного массива:\n', median(array, len(array) / 2))
