# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

# Решение для случая, когда элемент может встречаться в списке несколько раз.

import random

SIZE = 13
MIN_NUMB = -100
MAX_NUMB = 100
random_numbers = [random.randint(MIN_NUMB, MAX_NUMB + 1) for _ in range(SIZE)]
print(random_numbers)  # Вывод исключительно для удобства проверки.

max_negative = MIN_NUMB - 1
for numb in random_numbers:
    if numb < 0 and numb > max_negative:
        max_negative = numb
indexes_max_negative = []
for i in range(SIZE):
    if random_numbers[i] == max_negative:
        indexes_max_negative.append(i)
print(f'Максимальное отрицательное число в массиве: {max_negative}.')
print(f'Его позиция(и) в массиве: ', end='')
print(*indexes_max_negative, sep=', ', end='.')
