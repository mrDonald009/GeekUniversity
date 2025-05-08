
def info_user(**kwargs):
    for k, v in kwargs.items():
        print(k, v, end='; ')


info_user(phone_number='925', email='@', current_city='Moscow', birthday='22.03.1972', surname='Jhonson', name='Jack')