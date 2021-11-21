# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат и определить
# программы с наиболее эффективным использованием памяти.

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
import sys

SIZE = 13
MIN_NUMB = 0
MAX_NUMB = 99
random_numbers = [random.randint(MIN_NUMB, MAX_NUMB + 1) for _ in range(SIZE)]
print(random_numbers)


def change_1(random_numbers):
    memory = sys.getsizeof(random_numbers)
    min_numb = random_numbers[0]
    min_index = 0
    max_numb = random_numbers[0]
    max_index = 0
    for i in range(1, len(random_numbers)):
        if random_numbers[i] < min_numb:
            min_numb = random_numbers[i]
            min_index = i
        elif random_numbers[i] > max_numb:
            max_numb = random_numbers[i]
            max_index = i
    memory += (sys.getsizeof(min_index) + sys.getsizeof(max_index) + sys.getsizeof(min_numb) + sys.getsizeof(max_numb))
    random_numbers[min_index], random_numbers[max_index] = random_numbers[max_index], random_numbers[min_index]
    print(random_numbers)
    print(f'Поменяны местами элементы с индексами {min_index} и {max_index}')
    print(f'Затрачено памяти: {memory}')


change_1(random_numbers)


# Затрачено памяти: 304

def change_2(random_numbers):
    memory = sys.getsizeof(random_numbers)
    random_numbers[random_numbers.index(min(random_numbers))], random_numbers[
        random_numbers.index(max(random_numbers))] = random_numbers[random_numbers.index(max(random_numbers))], \
                                                     random_numbers[random_numbers.index(min(random_numbers))]
    print(f'Затрачено памяти: {memory}')


change_2(random_numbers)


# Затрачено памяти: 192

def change_3(random_numbers):
    memory = sys.getsizeof(random_numbers)
    min_index = random_numbers.index(min(random_numbers))
    memory += sys.getsizeof(min_index)
    max_index = random_numbers.index(max(random_numbers))
    memory += sys.getsizeof(max_index)
    random_numbers[min_index], random_numbers[max_index] = random_numbers[max_index], random_numbers[min_index]
    print(random_numbers)
    print(f'Затрачено памяти: {memory}')


change_3(random_numbers)
# Затрачено памяти: 248


# Python 3.7.6  64 разрядная система
# Вторая версия тратит меньше всего памяти, т.к. не создаётся промежуточных переменных.
# Первая версия самая затратная в плане памяти т.к. используется большое количество вспомогательных переменных.
