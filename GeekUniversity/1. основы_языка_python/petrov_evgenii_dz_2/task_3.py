#month = int(input('Введите месяц: '))

month = 8
seasons = {
    12: 'Зима',
    3: 'Весна',
    6: 'Лето',
    9: 'Осень'
}
if  month == 1 or month == 2 or month == 12 :
    print(seasons[12])
elif 3 <= month <= 5:
    print(seasons[3])
elif 6 <= month <= 8:
    print(seasons[6])
elif 9 <= month <= 11:
    print(seasons[9])

#num = int(input('Введите месяц: '))
num = 1
a = ['Зима', 'Весна', 'Лето', 'Осень']
if  num == 1 or num == 2 or num == 12 :
    print(a[0])
elif 3 <= num <= 5:
    print(a[1])
elif 6 <= num <= 8:
    print(a[2])
elif 9 <= num <= 11:
    print(a[3])
