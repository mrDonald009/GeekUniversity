

def fibo_gen():


    #number = int(input('Введите число: '))
    number = 4
    i = 1
    el = 1
    while i < number + 1:
        el = el * i
        i += 1
        yield el


for el in fibo_gen():
    print(el, end=' ')

