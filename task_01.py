# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них
# кратны каждому из чисел в диапазоне от 2 до 9.

MIN_DIVIDER = 2
MAX_DIVIDER = 9
LOW_RANGE = 2
HIGH_RANGE = 99
# Задание диапазонов делителей и числового массива, в котором необходимо искать кратные числа.

numbers_dividers = {num: 0 for num in range(MIN_DIVIDER, MAX_DIVIDER + 1)}
# Создание словаря, в котором ключами будут числа делители, а значениями - количество кратных им чисел в диапазоне.

for i in range(LOW_RANGE, HIGH_RANGE + 1):
    for j in range(MIN_DIVIDER, MAX_DIVIDER + 1):
        if i % j == 0:
            numbers_dividers[j] += 1

print(f'В диапазоне чисел от {LOW_RANGE} до {HIGH_RANGE}:')
for item in numbers_dividers.items():
    print(f'Количество чисел кратных {item[0]} : {item[1]}')
