# Задание 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего
# задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили
# замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.


def reverse_digit1(n):
    n2 = 0

    while n > 0:
        digit = n % 10
        n = n // 10
        n2 = n2 * 10
        n2 = n2 + digit
    return n2


def reverse_digit2(n):
    n2 = 0
    if n > 0:
        n = str(n)
        n_list = list(n)
        n_list.reverse()
        n2 = "".join(n_list)
    return n2


def reverse_digit3(n):
    # Показал лучшее время
    n2 = 0
    if n > 0:
        n = str(n)
        n2 = n[::-1]
    return n2


'''
1 способ:
reverse_digit1(234235546)
1000 loops, best of 5: 1.11 usec per loop
cProfile.run('reverse_digit1(234235546)')
4 function calls in 0.000 seconds
1    0.000    0.000    0.000    0.000 hw4ex1.py:15(reverse_digit1)
'''

'''
2 способ:
reverse_digit2(234235546)
1000 loops, best of 5: 733 nsec per loop
cProfile.run('reverse_digit2(234235546)')
6 function calls in 0.000 seconds
1    0.000    0.000    0.000    0.000 hw4ex1.py:26(reverse_digit2)
'''

'''
3 способ THE BEST TIME!:
reverse_digit3(234235546)
1000 loops, best of 5: 428 nsec per loop
cProfile.run('reverse_digit3(234235546)')
4 function calls in 0.000 seconds
1    0.000    0.000    0.000    0.000 hw4ex1.py:35(reverse_digit3)
'''