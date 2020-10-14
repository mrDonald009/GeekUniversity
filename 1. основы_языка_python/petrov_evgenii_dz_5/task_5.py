import json
my_list = ['2', '2', '3', '4', '5', '6', '7']
# while True:
#     a = input('Введите число: ')
#     if a:
#         res.append(a)
#     else:
#         break

with open('task_5_1.txt', 'w', encoding='utf-8') as a:
    for el in my_list:
        a.writelines(el + ' ')

with open('task_5_1.txt', 'r', encoding='utf-8') as b:
    list_numbers = (list(map(int, (b.read().split()))))
    first_sum = []
    sum_el = list_numbers[0] + list_numbers[1]
    first_sum.append(sum_el)
    i = 2

    for el in first_sum:

        while i < len(list_numbers):
            el += list_numbers[i]
            i += 1

    print(el)