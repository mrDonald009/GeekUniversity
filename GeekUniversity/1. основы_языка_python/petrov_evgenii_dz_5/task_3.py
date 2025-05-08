# res = []
# while True:
#     a = input('Введите фамилию сотрудника и его оклад: ')
#     if a:
#         res.append(a)
#     else:
#         break
#
# with open('task_3.txt', 'w', encoding='utf-8') as a:
#     for i in res:
#         a.write(i + '\n')


worker_list = []
salary_list = []
min_salary = []

with open('task_3_1.txt', 'r', encoding='utf-8') as a:

    for worker in a:
        worker_list.append(worker.strip().split())

    for i in worker_list:
        salary_list.append(i[1])

    sum_salary = list(map(float, salary_list))

    el = 0
    while el < len(sum_salary):
        if sum_salary[el] > 20000:
            el += 1
            continue
        min_salary.append(worker_list[el][0])
        el += 1

    print(f"сотрудники которые имеют оклад менее 20 тыс.: {(', '.join(min_salary))}")
    print(f'средняя величина дохода: {(sum(sum_salary)) / (len(salary_list))} рублей')


    # sum_list = [float(i) for i in salary_list]
    # print(sum_list)

    # for el in salary_list:
    #     sum_list.append(float(el))
    # print(sum_list)
