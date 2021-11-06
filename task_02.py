# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо
# заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно
# в этих позициях первого массива стоят четные числа.

import random

SIZE = 13
MIN_NUMB = 0
MAX_NUMB = 99
random_numbers = [random.randint(MIN_NUMB, MAX_NUMB + 1) for _ in range(SIZE)]
print(
    random_numbers)  # Вывод сгенерированного списка для того, чтобы можно было проверить правильность выполнения задания.
even_positions = []
for i in range(SIZE):
    if random_numbers[i] % 2 == 0:
        even_positions.append(i)
print('Позиции чётных элементов списка:', end=' ')
print(*even_positions, sep=', ', end='.')
