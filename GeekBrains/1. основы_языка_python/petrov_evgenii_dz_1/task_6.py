a = 2
b = 3
day = 1
while a <= b:
    a = a + a * 0.1
    day += 1
print(f'На {day} день спортсмен достиг результата - не менее {int(a)} км.')
