"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import timeit
from random import randint
from statistics import median

def without_sort(my_list):
    temp = my_list
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()

def another_way(my_list):
    temp_list = my_list
    for i in range(len(my_list) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)

m = randint(0, 10)
lst_obj = [randint(0, m) for _ in range(0, 2 * m + 1)]

print(lst_obj)
print(without_sort(lst_obj)) # Находжение медианы без сортировки массива
print(median(lst_obj)) # Нахождение медианы через встроенную функцию
print(another_way(lst_obj)) # Нахождение медианы путем удаление максимальных элементов


print(timeit.timeit('without_sort(lst_obj[:])', setup='from __main__ import lst_obj, without_sort', number=100))
print(timeit.timeit('median(lst_obj[:])', setup='from __main__ import lst_obj, median', number=100))
print(timeit.timeit('another_way(lst_obj)', setup='from __main__ import lst_obj, another_way', number=100))

"""
[5, 3, 2, 1, 3, 2, 3, 2, 1, 2, 4]
2
2
2
0.0015804000000000026
7.929999999999743e-05
5.609999999999643e-05

Нахождение медианы через функцию без сортировки быстрее, встроенной функции и функции путем удаления максимальных эл-ов.
"""