# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

letter_to_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                   'C': 12, 'D': 13, 'E': 14, 'F': 15}
digit_to_letter = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

print('Введите первое число')
num1 = list(input().upper())
print('Введите второе число')
num2 = list(input().upper())

if len(num2) > len(num1):
    num1, num2 = num2, num1
sum_digit = []
rest = 0
j = len(num2) - 1
for i in range(len(num1) - 1, -1, -1):
    if j >= 0:
        res = letter_to_digit[num1[i]] + letter_to_digit[num2[j]] + rest
        rest = res // 16
        if res % 16 <= 9:
            sum_digit.insert(0, res % 16)
        else:
            sum_digit.insert(0, digit_to_letter[res % 16])
        j -= 1
    else:
        res = letter_to_digit[num1[i]] + rest
        rest = res // 16
        if res % 16 <= 9:
            sum_digit.insert(0, res % 16)
        else:
            sum_digit.insert(0, digit_to_letter[res % 16])
if rest != 0:
    sum_digit.insert(0, res % 16)

print(*sum_digit, sep='')
