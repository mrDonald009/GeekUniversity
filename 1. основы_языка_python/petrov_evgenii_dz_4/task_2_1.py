numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

i = 0
res = []
while i < (len(numbers) - 1):
    if numbers[i] >= numbers[i + 1]:
        i += 1
        continue
    res.append(numbers[i + 1])
    i += 1
print(res)

