"""
Задание 2.
Предложить варианты оптимизации и доказать (наглядно, кодом) их эффективность
"""

import copy
from memory_profiler import profile


@profile
def func_1():
    x = list(range(100000))
    y = copy.deepcopy(x)
    return y
func_1()

@profile
def func_2():
    x = list(range(100000))
    y = copy.deepcopy(x)
    del x
    y = None
    return y
func_2()

'''
Line #    Mem usage    Increment   Line Contents
================================================
    10     14.9 MiB     14.9 MiB   @profile
    11                             def func_1():
    12     18.7 MiB      3.8 MiB       x = list(range(100000))
    13     20.2 MiB      1.5 MiB       y = copy.deepcopy(x)
    14     20.2 MiB      0.0 MiB       return y


Line #    Mem usage    Increment   Line Contents
================================================
    17     16.0 MiB     16.0 MiB   @profile
    18                             def func_2():
    19     19.5 MiB      3.5 MiB       x = list(range(100000))
    20     19.5 MiB      0.0 MiB       y = copy.deepcopy(x)
    21     18.7 MiB      0.0 MiB       del x
    22     16.0 MiB      0.0 MiB       y = None
    23     16.0 MiB      0.0 MiB       return y

Обе функции из массива, создают список, делают копию списка и возвращают значение копии.
Но в func_2() мы удаляем изначально созданный список, из за чего получаем разницу занимаемой памяти в 4,2 Mib.
'''