# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и
# отсортированный массивы. Сортировка должна быть реализована в виде функции. По
# возможности доработайте алгоритм (сделайте его умнее).

import random


def bubble(array):
    n = 1
    while n < len(array):
        counter = 0
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                counter += 1
        if counter == 0:
            break
        n += 1

    print(array)


array = [random.randrange(-100, 100) for _ in range(10)]
print(array)
bubble(array)
