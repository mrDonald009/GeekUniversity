"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

def average_profit():

    source = {}
    count_company = int(input('Введите количество предприятий для расчета прибыли: '))

    def average_value(value, num=0, count=0):  # функция получает среднюю цену
        for el in value:
            num += int(el)
            count += 1
        return num / count

    for company in range(count_company):  # для каждой компании создаем пару ключ, значение
        name_company = input('Введите название предприятия: ')
        profit_company = (input('через пробел введите прибыль данного предприятия за каждый квартал:')).split()
        source.setdefault(name_company, profit_company)

    average_year = (sum(source.values(), []))  # переменная хранит все цены компаний
    print(f'Средняя годовая прибыль всех предприятий: {average_value(average_year)}')

    over_average = []
    under_average = []
    for el in source.keys():
        if average_value(source.get(el)) > average_value(average_year):
            under_average.append(el)
        else:
            over_average.append(el)
    print(f'Предприятия, с прибылью выше среднего значения: {", ".join(under_average)}')
    print(f'Предприятия, с прибылью ниже среднего значения: {", ".join(over_average)}')

average_profit()