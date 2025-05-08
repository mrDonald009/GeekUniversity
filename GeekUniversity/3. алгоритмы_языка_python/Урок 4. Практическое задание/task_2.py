"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

import timeit

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def reverse_numbers(num):
    return (int(str(num)[::-1]))


num = 123456789

print(recursive_reverse(num))
print(reverse_numbers(num))

print(
    timeit.timeit(
        'recursive_reverse(num)',
        setup='from __main__ import recursive_reverse,num',
        number=10000
    )
)

print(
    timeit.timeit(
        'reverse_numbers(num)',
        setup='from __main__ import reverse_numbers,num',
        number=10000
    )
)