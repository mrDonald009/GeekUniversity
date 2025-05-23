"""
Задание 4.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

#------------------------------------------------------------------------

users = {
    'person_1': {'password': 1, 'status': 'active'},
    'person_2': {'password': 12, 'status': 'inactive'},
    'person_3': {'password': 123, 'status': 'active'},
    'person_4': {'password': 1234, 'status': 'inactive'},
    'person_5': {'password': 12345, 'status': 'active'}
}

#------------------------------------------------------------------------
                                                                                                     # Всего O(1)
def authorization(users, user_name, user_password):
    if users.get(user_name):                                                                               # O(1)
        if users[user_name]['password'] == user_password and users[user_name]['status'] == 'active':       # O(1)
            print('Доступ разрешен.')                                                                      # O(1)
        elif users[user_name]['password'] == user_password and users[user_name]['status'] == 'inactive':   # O(1)
            print('Доступ запрещен, пройдите активацию.')                                                  # O(1)
        elif users[user_name]['password'] != user_password:                                                # O(1)
            print('Доступ запрещен.')                                                                      # O(1)
    else:                                                                                                  # O(1)
        print('Неверный логин.')                                                                           # O(1)

authorization(users, 'person_1', 1)

#------------------------------------------------------------------------
                                                              # Всего O(N)
def activator(log, pas):
    for k, v in users.items():                                      # O(N)
        if k == log:                                                # O(1)
            if v['password'] == pas and v['status'] == 'active':    # O(1)
                print('Доступ разрешен.')                           # O(1)
                break                                               # O(1)
            if v['password'] == pas and v['status'] != 'inactive':  # O(1)
                print('Доступ запрещен, пройдите активацию.')       # O(1)
                break                                               # O(1)
            if v['password'] != pas:                                # O(1)
                print('Пароль неверный.')                           # O(1)
                break                                               # O(1)
        print('Неверный логин.')                                    # O(1)
        break                                                       # O(1)

activator('person_1', 3)

#------------------------------------------------------------------------
                                                              # Всего O(N)
def activation():
    person = input('Введите логин: ')                               # O(1)
    if person in users:                                             # O(N)
        pas = int(input('Введите пароль: '))                        # O(1)
        if pas == users[person]['password']:                        # O(1)
            if users[person]['status'] == 'active':                 # O(1)
                print('Доступ разрешен.')                           # O(1)
            else:
                print('Доступ запрещен, пройдите активацию.')       # O(1)
        else:
            print('Пароль неверный.')                               # O(1)
    else:
        print('Логин неверный.')                                    # O(1)

activation()

#------------------------------------------------------------------------

# Первый вариант лучший, так как у него самая низкая сложность.