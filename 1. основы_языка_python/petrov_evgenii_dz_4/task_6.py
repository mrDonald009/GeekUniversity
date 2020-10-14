from itertools import count, cycle


def endless_iter():
    #number = int(input('Введите число: '))
    number = 5
    for el in count(number):
        if el > number:
            print(el)


def eternal_list():
    my_list = [1, 'a', 2, True, 'b',  3, 'c', 4]
    for el in cycle(my_list):
        print(el)

