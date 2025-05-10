#num = int(input('Введите значение: '))

num = 10
my_list = [7, 5, 3, 3, 2]
i = 0
while i < len(my_list):
    if my_list[i] == num:
        my_list.insert(i, num)
        print(my_list)
        break
    elif my_list[i] > num:
        i += 1
        continue
    my_list.insert(i, num)
    print(my_list)
    break
else:
    my_list.append(num)
    print(my_list)












