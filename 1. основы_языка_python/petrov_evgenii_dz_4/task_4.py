numbers = [1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7, 7]
result = [number for number in numbers if numbers.count(number) < 2]
print(result)