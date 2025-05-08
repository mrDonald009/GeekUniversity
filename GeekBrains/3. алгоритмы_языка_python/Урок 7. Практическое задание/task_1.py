"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
import timeit

def my_list(num):

    my_list = [random.randint(-100, 99) for _ in range(num)]
    return my_list

def bubble_sort(lst_obj):

    print(lst_obj)
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    print(lst_obj)

#bubble_sort(my_list(10))
print(timeit.timeit("bubble_sort(my_list(10))", setup="from __main__ import bubble_sort, my_list", number=1))
print(timeit.timeit("bubble_sort(my_list(20))", setup="from __main__ import bubble_sort, my_list", number=1))
print((timeit.timeit("bubble_sort(my_list(30))", setup="from __main__ import bubble_sort, my_list", number=1)), '\n', "-" * 45)


def my_list_1(num):

    my_list = [random.randint(-100, 99) for _ in range(num)]
    return my_list

def bubble_sort_1(lst_obj):

    print(lst_obj)
    n = 1
    while n < len(lst_obj):
        signal = True
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                signal = False
        if signal:
            break
        n += 1
    print(lst_obj)

#bubble_sort_1(my_list_1(10))
print(timeit.timeit("bubble_sort_1(my_list_1(10))", setup="from __main__ import bubble_sort_1, my_list_1", number=1))
print(timeit.timeit("bubble_sort_1(my_list_1(20))", setup="from __main__ import bubble_sort_1, my_list_1", number=1))
print(timeit.timeit("bubble_sort_1(my_list_1(30))", setup="from __main__ import bubble_sort_1, my_list_1", number=1))

"""
[-65, 69, 3, 69, 88, 46, 84, 55, -27, -90]
[88, 84, 69, 69, 55, 46, 3, -27, -65, -90]
6.820000000000437e-05
[40, 6, -82, -36, -21, 42, 7, 63, 76, -99, -8, -11, -29, -88, 44, -67, 81, 7, -52, 96]
[96, 81, 76, 63, 44, 42, 40, 7, 7, 6, -8, -11, -21, -29, -36, -52, -67, -82, -88, -99]
8.69999999999968e-05
[46, -16, 22, -75, -82, -6, -83, -62, -26, -9, -22, -8, 45, -27, 54, -56, -50, -51, -19, 54, 35, -83, -34, 46, -67, 85, -32, 0, -75, -31]
[85, 54, 54, 46, 46, 45, 35, 22, 0, -6, -8, -9, -16, -19, -22, -26, -27, -31, -32, -34, -50, -51, -56, -62, -67, -75, -75, -82, -83, -83]
0.00013900000000000023 
 ---------------------------------------------
[-68, -72, 58, 66, 15, 26, -93, -73, -33, 54]
[66, 58, 54, 26, 15, -33, -68, -72, -73, -93]
4.300000000000137e-05
[4, 36, -71, 39, -28, 85, 5, 23, 51, -91, 54, -89, -35, 59, -54, -92, -55, -28, -52, 34]
[85, 59, 54, 51, 39, 36, 34, 23, 5, 4, -28, -28, -35, -52, -54, -55, -71, -89, -91, -92]
7.800000000000168e-05
[93, 33, 31, -74, 67, 93, -97, -9, -35, 94, -4, -13, 38, -89, -20, -31, -57, 70, 40, 91, -38, -94, -81, 80, -18, 19, -9, 80, 47, 15]
[94, 93, 93, 91, 80, 80, 70, 67, 47, 40, 38, 33, 31, 19, 15, -4, -9, -9, -13, -18, -20, -31, -35, -38, -57, -74, -81, -89, -94, -97]
0.00013329999999999592

После изменения программы можно сделать вывод, что код стал работать быстрее.
"""