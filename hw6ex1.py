# Задание 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с
# кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

import sys


def show_size(x, level=0):
    print('\t' * level, f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)

        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


# Программа возвращает число в обратном порядке
def reverse_digit1(n):
    n2 = 0

    while n > 0:
        digit = n % 10
        n = n // 10
        n2 = n2 * 10
        n2 = n2 + digit
    return locals()


def reverse_digit2(n):
    n2 = 0
    if n > 0:
        n = str(n)
        n_list = list(n)
        n_list.reverse()
        n2 = "".join(n_list)
    return locals()


def reverse_digit3(n):
    # лучшее время
    # меньший объем памяти
    n2 = 0
    if n > 0:
        n = str(n)
        n2 = n[::-1]
    return locals()


print('*' * 100 + '\n1 способ:')
print(show_size(reverse_digit1(6556499797)))
print('*' * 100 + '\n2 способ:')
print(show_size(reverse_digit2(6556499797)))
print('*' * 100 + '\n3 способ:')
print(show_size(reverse_digit3(6556499797)))
print('*' * 100)
print(sys.version, sys.platform)

# Третий способ занимает меньший объем памяти, так как используется меньше всего переменных, а также не использует
# списки
'''
****************************************************************************************************
1 способ:
 type = <class 'dict'>, size = 232, object = {'n': 0, 'n2': 7979946556, 'digit': 6}
	 type = <class 'tuple'>, size = 56, object = ('n', 0)
		 type = <class 'str'>, size = 50, object = n
		 type = <class 'int'>, size = 24, object = 0
	 type = <class 'tuple'>, size = 56, object = ('n2', 7979946556)
		 type = <class 'str'>, size = 51, object = n2
		 type = <class 'int'>, size = 32, object = 7979946556
	 type = <class 'tuple'>, size = 56, object = ('digit', 6)
		 type = <class 'str'>, size = 54, object = digit
		 type = <class 'int'>, size = 28, object = 6
None
****************************************************************************************************
2 способ:
 type = <class 'dict'>, size = 232, object = {'n': '6556499797', 'n2': '7979946556', 'n_list': ['7', '9', '7', '9', '9', '4', '6', '5', '5', '6']}
	 type = <class 'tuple'>, size = 56, object = ('n', '6556499797')
		 type = <class 'str'>, size = 50, object = n
		 type = <class 'str'>, size = 59, object = 6556499797
	 type = <class 'tuple'>, size = 56, object = ('n2', '7979946556')
		 type = <class 'str'>, size = 51, object = n2
		 type = <class 'str'>, size = 59, object = 7979946556
	 type = <class 'tuple'>, size = 56, object = ('n_list', ['7', '9', '7', '9', '9', '4', '6', '5', '5', '6'])
		 type = <class 'str'>, size = 55, object = n_list
		 type = <class 'list'>, size = 136, object = ['7', '9', '7', '9', '9', '4', '6', '5', '5', '6']
			 type = <class 'str'>, size = 50, object = 7
			 type = <class 'str'>, size = 50, object = 9
			 type = <class 'str'>, size = 50, object = 7
			 type = <class 'str'>, size = 50, object = 9
			 type = <class 'str'>, size = 50, object = 9
			 type = <class 'str'>, size = 50, object = 4
			 type = <class 'str'>, size = 50, object = 6
			 type = <class 'str'>, size = 50, object = 5
			 type = <class 'str'>, size = 50, object = 5
			 type = <class 'str'>, size = 50, object = 6
None
****************************************************************************************************
3 способ:
 type = <class 'dict'>, size = 232, object = {'n': '6556499797', 'n2': '7979946556'}
	 type = <class 'tuple'>, size = 56, object = ('n', '6556499797')
		 type = <class 'str'>, size = 50, object = n
		 type = <class 'str'>, size = 59, object = 6556499797
	 type = <class 'tuple'>, size = 56, object = ('n2', '7979946556')
		 type = <class 'str'>, size = 51, object = n2
		 type = <class 'str'>, size = 59, object = 7979946556
None
****************************************************************************************************
3.9.4 (v3.9.4:1f2e3088f3, Apr  4 2021, 12:32:44) 
[Clang 6.0 (clang-600.0.57)] darwin'''
