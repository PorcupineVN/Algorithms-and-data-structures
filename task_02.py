# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

print('Введите натуральное число')
numb = int(input())
even_digits_counter = 0
odd_digits_counter = 0
while numb != 0:
    if numb % 10 % 2 == 0:
        even_digits_counter += 1
    else:
        odd_digits_counter += 1
    numb = numb // 10
print(f'В ведённом числе {even_digits_counter} чётных цифр и {odd_digits_counter} нечётных')
