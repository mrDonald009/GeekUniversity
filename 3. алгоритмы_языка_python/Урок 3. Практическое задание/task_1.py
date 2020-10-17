"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time


def list_time(num):

    start = time.time()
    numbers = []
    for el in range(1, num + 1):
        numbers.append(el)
    finish = time.time()
    print(f'Заполнение списка в {num} элементов заняло {finish - start} сек.')

    if numbers[499000] in numbers:
        finish_1 = time.time()
        print(f'Извлечение элемента из спискав {num} элементов заняло {finish_1 - start} сек.')

list_time(1000000)

def dict_time(num):

    start = time.time()
    numbers = dict()
    for el in range(1, num + 1):
        numbers.setdefault(el)
    finish = time.time()
    print(f'Заполнение словаря в {num} элементов заняло {finish - start} сек.')

    if numbers.get(499000) == None:
        finish_1 = time.time()
        print(f'Извлечение элемента из словаря в {num} элементов заняло {finish_1 - start} сек.')

dict_time(1000000)

import time
start_1 = time.time()
res = []
for i in range(1000):
    res.append(i)
    res.index(i)
print(res)
finish_1 = time.time()
print(finish_1 - start_1)

stert_2 = time.time()
res = dict()
for el in range(1000):
    res[el] = el
    res.get(el)
print(res)
finish_2 = time.time()
print(finish_2 - stert_2)