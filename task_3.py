# По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y = kx + b, проходящей через эти точки.

print('Введите координату Х первой точки')
x1 = float(input())
print('Введите координату Y первой точки')
y1 = float(input())
print('Введите координату Х второй точки')
x2 = float(input())
print('Введите координату Y второй точки')
y2 = float(input())
if x1==x2:
    print(f'X = {x1}')
else:
    if y1==y2:
        print(f'Y = {y1}')
    else:
        k = round((y1-y2)/(x1-x2), 2)
        b = round(y2 - k*x2, 2)
        if b <= 0:
            print(f'y = {k}x{b}')
        else:
            print(f'y= {k}x+{b}')