#second = int(input('Введите время в секундах: '))
second = 4561
hour = second // 3600
minute = (second - 3600) / 60
sec = int((minute * 100) % 100)

print(f'{hour}:{int(minute)}:{sec}')