#a = input('Введите элементы: ')

a = 'spisok'
b = list(a)
i = 0
k = 0

while i < len(b):
    b.insert(k, b[k+1])
    k += 2
    b.pop(k)
    i += 1
    print(b)
