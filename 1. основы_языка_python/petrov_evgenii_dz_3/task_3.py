

def my_func(a, b, c):

    numbers = [a, b, c]
    number = min(numbers)
    numbers.remove(number)
    return sum(numbers)


print(my_func(5,7,9))