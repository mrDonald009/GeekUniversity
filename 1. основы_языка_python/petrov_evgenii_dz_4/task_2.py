numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def my_fun():
    i = 0
    while i < (len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            i += 1
            continue
        el = numbers[i + 1]
        yield el
        i += 1


for el in my_fun():
    print(el, end=' ')