

def func():
    with open('task_2_1.txt', encoding='utf-8') as a:
        for sting in a:
            yield f"{len(sting.split(' '))} слов(а)"


for ind, el in enumerate(func(), 1):
    print(f'в {ind} строке - {el}')

