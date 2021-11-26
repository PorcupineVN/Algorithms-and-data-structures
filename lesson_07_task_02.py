# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный
# массивы.

import random


def quick_sort(data, first, last):
    if first >= last:
        return

    pivot = data[random.randint(first, last)]
    i = first
    j = last

    while i <= j:
        while data[i] < pivot:
            i += 1
        while data[j] > pivot:
            j -= 1
        if i <= j:
            data[i], data[j] = data[j], data[i]
            i, j = i + 1, j - 1

    quick_sort(data, first, j)
    quick_sort(data, i, last)


array = [random.uniform(0, 50) for _ in range(10)]
print(array)
quick_sort(array, 0, len(array) - 1)
print(array)
