# 9.Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

max_summ = 0
max_numb = 0
user_numb = int(input('Введите натуральное число: '))
while user_numb != 0:
    summ_digits = 0
    ghost_user_numb = user_numb
    while ghost_user_numb != 0:
        summ_digits += ghost_user_numb % 10
        ghost_user_numb = ghost_user_numb // 10
    if summ_digits > max_summ:
        max_summ = summ_digits
        max_numb = user_numb
    user_numb = int(input('Введите натуральное число: '))
print(f'Число с максимальной суммой цифр: {max_numb}, сумма его цифр: {max_summ}')
