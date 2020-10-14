from functools import reduce


def func(prev_el, el):
    return prev_el * el


res = [number for number in range(100, 1000 +1) if number % 2 == 0]

print(res)
print(reduce(func, res))
