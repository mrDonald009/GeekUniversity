

def devider(a, b):
    #a = int(input('Введите делимое: '))
    #b = int(input('Ведите делитель: '))
    if b != 0:
        return a / b
    else:
        print('На ноль делить нельзя, попробуйте снова: ')
        devider()



print(devider(49, 7))



