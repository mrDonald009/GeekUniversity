

def enter():
    res = []
    while True:
        abc = input('Введите числа: ')
        if abc != 'ok':
            func(abc)
            res.append(func(abc))
            print(sum(res))
        else:
            print(sum(res))
            break


def func(abc):
    abc.split()
    i = 0
    b = []
    while i < len(abc):
        if abc[i] != ' ':
            b.append(int(abc[i]))
            i += 1
        else:
            i += 1

    c = sum(b)
    return c


enter()

