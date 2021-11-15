# 2). Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее
# простое число. Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import cProfile
import timeit


def eratosfen(element):
    n = 1000
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    for i in enumerate(res):
        if i[0] == element - 1:
            return i[1]


print(timeit.timeit('eratosfen(10)', number=1000, globals=globals()))  # 0.2733464
print(timeit.timeit('eratosfen(20)', number=1000, globals=globals()))  # 0.2690249
print(timeit.timeit('eratosfen(30)', number=1000, globals=globals()))  # 0.29106960000000004
print(timeit.timeit('eratosfen(40)', number=1000, globals=globals()))  # 0.27748189999999995
print(timeit.timeit('eratosfen(50)', number=1000, globals=globals()))  # 0.28798239999999997
print(timeit.timeit('eratosfen(75)', number=1000, globals=globals()))  # 0.29039360000000003
print(timeit.timeit('eratosfen(100)', number=1000, globals=globals()))  # 0.2763340000000001
print(timeit.timeit('eratosfen(666)', number=1000, globals=globals()))  # 0.2802205

cProfile.run('eratosfen(13)')
"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_02.py:15(eratosfen)
        1    0.000    0.000    0.000    0.000 task_02.py:17(<listcomp>)
        1    0.000    0.000    0.000    0.000 task_02.py:27(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


def not_eratosfen(i):
    arr = [2]
    x = 3
    while len(arr) < i:
        for j in arr:
            if x % j == 0:
                break
        else:
            arr.append(x)
        x += 1
    return arr[i - 1]


print(timeit.timeit('not_eratosfen(10)', number=1000, globals=globals()))  # 0.007440000000000335
print(timeit.timeit('not_eratosfen(20)', number=1000, globals=globals()))  # 0.021206600000000186
print(timeit.timeit('not_eratosfen(30)', number=1000, globals=globals()))  # 0.040036699999999925
print(timeit.timeit('not_eratosfen(40)', number=1000, globals=globals()))  # 0.06612780000000029
print(timeit.timeit('not_eratosfen(50)', number=1000, globals=globals()))  # 0.0964391
print(timeit.timeit('not_eratosfen(75)', number=1000, globals=globals()))  # 0.19653739999999997
print(timeit.timeit('not_eratosfen(100)', number=1000, globals=globals()))  # 0.3410660999999999
print(timeit.timeit('not_eratosfen(666)', number=1000, globals=globals()))  # 11.740866700000002

cProfile.run('not_eratosfen(13)')

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_02.py:53(not_eratosfen)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       40    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       12    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
1 алгоритм имеет константную сложность и достаточно высокое быстродействие
2 алгоритм имеет логарифмическую сложность (не уверен) и показывает лучшее быстродействие на малых числах, 
но много худшее на больших
"""
