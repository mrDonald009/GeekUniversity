#a = input('Введите предложение: ')

a = 'несколько слов через пробелпробел'
a.split()
i = 1
for el in a.split():
    if len(el) < 10:
        print(i, el)
        i += 1
    else:
        print(i, el[:10])
        i += 1
