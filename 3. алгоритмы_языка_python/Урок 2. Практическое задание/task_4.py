"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def abc(n,numbers=[1, -0.5, 0.25, -0.125],el=0,res=0):

    if n == 1:
        print(f'Количество элементов - 1, их сумма - {numbers[el]}.')

    elif n != el:
        res += numbers[el]
        el += 1
        abc(n, numbers, el, res)

    else:
        print(f'Количество элементов - {n}, их сумма - {res}')

abc(4)