# Задание 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность
# алгоритмов.

import math
import cProfile


def border_func(i):
    '''
    Количество простых чисел на отрезке [1, n] растёт с увеличением n как n / ln(n)
    :param i: Количество простых чисел
    :return: Верхняя граница отрезка, состоящего из i простых чисел
    '''

    number_of_primes = 0
    border = 2
    while number_of_primes <= i:
        number_of_primes = border / math.log(border)
        border += 1
    return border


def sieve(count):
    '''
    Метод "Решето Эратосфена"
    :param count: порядковый номер простого числа
    :return: i-ое по счету простое число
    '''

    border = border_func(count)
    sieve_list = [i for i in range(border + 1)]
    sieve_list[1] = 0
    for i in range(2, border):
        if sieve_list[i] != 0:
            j = i * 2
            while j < border:
                sieve_list[j] = 0
                j += i
    result = [i for i in sieve_list if i != 0]
    return result[count - 1]


def prime(i):
    '''
    Без использования метода "Решето Эратосфена"
    :param i: порядковый номер простого числа
    :return: i-ое по счету простое число
    '''

    prime_list = [2]
    border = 3
    while len(prime_list) < i:
        flag = True
        for j in prime_list.copy():
            if border % j == 0:
                flag = False
                break
        if flag:
            prime_list.append(border)
        border += 1
    return prime_list[-1]


# sieve(10)
# 1000 loops, best of 5: 12 usec per loop
# cProfile.run('sieve(10)')
# 42 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 hw4ex2.py:24(sieve)

# sieve(50)
# 1000 loops, best of 5: 96.4 usec per loop
# cProfile.run('sieve(50)')
# 289 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 hw4ex2.py:24(sieve)

# sieve(100)
# 1000 loops, best of 5: 248 usec per loop
# cProfile.run('sieve(100)')
# 654 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 hw4ex2.py:24(sieve)

# sieve(1000)
# 1000 loops, best of 5: 3.79 msec per loop
# cProfile.run('sieve(1000)')
# 9125 function calls in 0.008 seconds
# 1    0.003    0.003    0.008    0.008 hw4ex2.py:24(sieve)

# prime(10)
# 1000 loops, best of 5: 6.93 usec per loop
# cProfile.run('prime(10)')
# 68 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 hw4ex2.py:44(prime)

# prime(50)
# 1000 loops, best of 5: 94.3 usec per loop
# cProfile.run('prime(50)')
# 508 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 hw4ex2.py:44(prime)

# prime(100)
# 1000 loops, best of 5: 359 usec per loop
# cProfile.run('prime(100)')
# 1182 function calls in 0.001 seconds
# 1    0.001    0.001    0.001    0.001 hw4ex2.py:44(prime)

# prime(1000)
# 1000 loops, best of 5: 29.3 msec per loop
# cProfile.run('prime(1000)')
# 16838 function calls in 0.051 seconds
# 1    0.042    0.042    0.051    0.051 hw4ex2.py:44(prime)
