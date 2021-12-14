# Задание 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

size = 20
array = [random.randint(-100, 100) for i in range(size)]
print('Исходный массив:\n', array)


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


bubble_sort(array)
print('Отсортированный по убыванию массив:\n', array)
