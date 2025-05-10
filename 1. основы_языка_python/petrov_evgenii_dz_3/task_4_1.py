

def my_func(x, y):
    num = abs(y)
    i = 1
    z = x
    while i < num:
        x *= z
        i += 1
    print(1 / x)


my_func(10, -2)

