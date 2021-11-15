# 1). Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках
# домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы
# проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# Определить, какое число в массиве встречается чаще всего.
import random
import timeit
import cProfile


# Вариант №1

def popular_numbers_1(random_numbers):
    dict_numbers = {}
    for numb in random_numbers:
        if numb in dict_numbers.keys():
            dict_numbers[numb] += 1
        else:
            dict_numbers[numb] = 1
    most_popular = 0
    for value in dict_numbers.values():
        if value > most_popular:
            most_popular = value
    popular_numbers = []
    for key, value in dict_numbers.items():
        if value == most_popular:
            popular_numbers.append(key)
    return popular_numbers


print(timeit.timeit('popular_numbers_1([random.randint(0, 100) for _ in range(10)])', number=1000,
                    globals=globals()))  # 0.014962599999999993
print(timeit.timeit('popular_numbers_1([random.randint(0, 100) for _ in range(100)])', number=1000,
                    globals=globals()))  # 0.13018649999999998
print(timeit.timeit('popular_numbers_1([random.randint(0, 100) for _ in range(1000)])', number=1000,
                    globals=globals()))  # 1.2021193000000001

cProfile.run('popular_numbers_1([random.randint(0, 100) for _ in range(1000)])')


#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<listcomp>)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#      1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
#      1000    0.000    0.000    0.001    0.000 random.py:218(randint)
#      1000    0.000    0.000    0.001    0.000 random.py:224(_randbelow)
#         1    0.000    0.000    0.000    0.000 task_01.py:19(popular_numbers_1)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1285    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#      1000    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
#         1    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}

# Вариант №2
def popular_numbers_2(random_numbers):
    num = None
    frequency = 0

    for item in random_numbers:
        el = random_numbers.count(item)
        if el > frequency:
            frequency = el
            num = item
    return num, frequency


print(timeit.timeit('popular_numbers_2([random.randint(0, 100) for _ in range(10)])', number=1000,
                    globals=globals()))  # 0.013131900000000085
print(timeit.timeit('popular_numbers_2([random.randint(0, 100) for _ in range(100)])', number=1000,
                    globals=globals()))  # 0.26119990000000004
print(timeit.timeit('popular_numbers_2([random.randint(0, 100) for _ in range(1000)])', number=1000,
                    globals=globals()))  # 16.6521426

cProfile.run('popular_numbers_2([random.randint(0, 100) for _ in range(1000)])')


# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<listcomp>)
#        1    0.000    0.000    0.018    0.018 <string>:1(<module>)
#     1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
#     1000    0.000    0.000    0.001    0.000 random.py:218(randint)
#     1000    0.000    0.000    0.001    0.000 random.py:224(_randbelow)
#        1    0.000    0.000    0.016    0.016 task_01.py:64(popular_numbers_2)
#        1    0.000    0.000    0.018    0.018 {built-in method builtins.exec}
#     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1000    0.016    0.000    0.016    0.000 {method 'count' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1274    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

def popular_numbers_3(random_numbers):
    x = 0
    max_count = 0
    num = 0
    for i in list(set(random_numbers)):
        for el in random_numbers:
            if i == el:
                x += 1
        if x >= max_count:
            max_count = x
            num = i
        x = 0
    return num, max_count


print(timeit.timeit('popular_numbers_3([random.randint(0, 100) for _ in range(10)])', number=1000,
                    globals=globals()))  # 0.016094400000000064
print(timeit.timeit('popular_numbers_3([random.randint(0, 100) for _ in range(100)])', number=1000,
                    globals=globals()))  # 0.28465890000000016
print(timeit.timeit('popular_numbers_3([random.randint(0, 100) for _ in range(1000)])', number=1000,
                    globals=globals()))  # 3.7336808999999995

cProfile.run('popular_numbers_3([random.randint(0, 100) for _ in range(1000)])')

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.002    0.002 <string>:1(<listcomp>)
#        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#     1000    0.001    0.000    0.001    0.000 random.py:174(randrange)
#     1000    0.000    0.000    0.002    0.000 random.py:218(randint)
#     1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
#        1    0.003    0.003    0.003    0.003 task_01.py:86(popular_numbers_3)
#        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1303    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

"""
1 вариант имеет линейную сложность и демонстрирует самую быструю работу на больших массивах.
2 вариант имеет квадратичную??? (не уверен) сложность и демонстрирует самую медленную работу.
3 вариант имеет линейную (терзают сомнения) сложность, демонстрирует средний результат. 

Лучший результат демонстрирует 1 вариант алгоритма, он значительно быстрее остальных. 

"""
