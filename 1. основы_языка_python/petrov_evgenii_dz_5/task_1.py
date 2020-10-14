# res = []
# while True:
#     a = input('Введите строку: ')
#     if a:
#         res.append(a)
#     else:
#         break
res = ['строка_1', 'строка_2', 'строка_3', 'строка_4']

with open('task_1_1.txt', 'w', encoding='utf-8') as a:
    for el in res:
        a.write(el + '\n')
