#revenue = int(input('Введите значение выручки: '))
#costs = int(input('Введите значение издержки: '))

revenue = 300
costs = 200
worker = 5

if revenue > costs:
    print('У вашей компании есть прибыль')
    profitability = revenue / (revenue - costs)
    #worker = int(input('Введите кол-во сотрудников: '))
    worker_profit = (revenue - costs) / worker

else:
    print('У вашей компании есть убыток')