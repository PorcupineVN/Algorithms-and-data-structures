# 4. Определить, какое число в массиве встречается чаще всего.

# В процессе тестов, неоднократно возникали ситуации нескольких самых популярных чисел. Так что решение реализовано
# для случая не очень идеального пользователя.
import random

SIZE = 13
MIN_NUMB = 0
MAX_NUMB = 10
random_numbers = [random.randint(MIN_NUMB, MAX_NUMB + 1) for _ in range(SIZE)]
print(random_numbers)  # Традиционный вывод для удобства проверки.

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
print(f'Чаще всего ({most_popular} раз(а)) встречаются числа: ', end='')
print(*popular_numbers, sep=', ', end='.')

# P.S. Не отсортировал т.к. на лекции было озвучено требование не использовать встроенные методы.
