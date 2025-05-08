"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

from memory_profiler import profile

@profile()
def func_1(number):
    res = []
    [res.append(num) for num in range(number) if num % 2 == 0]
    return res
func_1(10000)

@profile()
def func_2(number):
    res = []
    for i in range(number):
        if i % 2 == 0:
            res.append(i)
            return res
func_2(10000)

'''
Line #    Mem usage    Increment   Line Contents
================================================
    19     14.9 MiB     14.9 MiB   @profile()
    20                             def func_1(number):
    21     14.9 MiB      0.0 MiB       res = []
    22     15.2 MiB      0.1 MiB       [res.append(num) for num in range(number) if num % 2 == 0]
    23     15.2 MiB      0.0 MiB       return res

Line #    Mem usage    Increment   Line Contents
================================================
    26     15.2 MiB     15.2 MiB   @profile()
    27                             def func_2(number):
    28     15.2 MiB      0.0 MiB       res = []
    29     15.2 MiB      0.0 MiB       for i in range(number):
    30     15.2 MiB      0.0 MiB           if i % 2 == 0:
    31     15.2 MiB      0.0 MiB               res.append(i)
    32     15.2 MiB      0.0 MiB               return res

Обе функции добавлют (четные) элементы из массивав в список, а затем возвращают значение в виде получившегося списка.
func_1 работает через генератор, а func_2 через цикл.
func_1 работает на 0,3 Mib быстрее.'''