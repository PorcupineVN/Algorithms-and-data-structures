# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 13
MIN_NUMB = 0
MAX_NUMB = 99
random_numbers = [random.randint(MIN_NUMB, MAX_NUMB + 1) for _ in range(SIZE)]
print(random_numbers)

min_numb = random_numbers[0]
min_index = 0
max_numb = random_numbers[0]
max_index = 0
for i in range(1, SIZE):
    if random_numbers[i] < min_numb:
        min_numb = random_numbers[i]
        min_index = i
    elif random_numbers[i] > max_numb:
        max_numb = random_numbers[i]
        max_index = i
random_numbers[min_index], random_numbers[max_index] = random_numbers[max_index], random_numbers[min_index]
print(random_numbers)
print(f'Поменяны местами элементы с индексами {min_index} и {max_index}')