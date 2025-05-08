"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from collections import deque

def person_is_seller(name):
    if name == 'lara':
        return True

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + ' - продавец манго')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


graph = {}
graph['jhonn'] = ['tanya', 'lana', 'lara']
graph['tanya'] = ['olya', 'gleb', 'oleg', 'roma']
graph['lana'] = ['lada', 'sofa']
graph['lara'] = ['mery']
graph['olya'] = ['edik', 'irina']

search('jhonn')