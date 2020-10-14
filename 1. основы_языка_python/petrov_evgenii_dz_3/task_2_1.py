

def show_user_info(**kwargs):
    person = {
        'name': '',
        'surname': '',
        'birthday': '',
        'current_city': '',
        'email': '',
        'phone_number': ''
    }
    for key in person.keys():
        person[key] = input(f'Введите {key}: ')
    for k, v in person.items():
        print(k, v, end='; ')


show_user_info()
