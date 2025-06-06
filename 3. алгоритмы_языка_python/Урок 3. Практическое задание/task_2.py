"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
from uuid import uuid4
import hashlib

password = input('Введите пароль: ')
salt = uuid4().hex
seq_passowrd = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
print(seq_passowrd)

repeat_passowrd = input('Введите пароль еще раз: ')
seq_repeat_passowrd = hashlib.sha256(salt.encode() + repeat_passowrd.encode()).hexdigest()

if seq_passowrd == seq_repeat_passowrd:
    print('Пароль верный.')
else:
    print('Пароль неверный.')
