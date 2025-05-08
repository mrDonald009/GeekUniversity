

users = {
    'person_1': {'password': 1, 'status': 'active'},
    'person_2': {'password': 12, 'status': 'inactive'},
    'person_3': {'password': 123, 'status': 'active'},
    'person_4': {'password': 1234, 'status': 'inactive'},
    'person_5': {'password': 12345, 'status': 'active'}
}


def activator(log, pas, stat):
    for k, v in users.items():
        if k == log:
            if v['password'] == pas and v['status']  == stat:
                print('Доступ разрешен.')
                break
            if v['password'] == pas and v['status'] != stat:
                print('Доступ запрещен, пройдите активацию.')
                break
            if v['password'] != pas:
                print('Пароль неверный.')
                break
        print('Неверный логин.')
        break

activator('person_1', 1, 'inactive')