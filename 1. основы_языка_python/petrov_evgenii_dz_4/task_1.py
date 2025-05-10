

def calc_salary():


    salary = {

        'выборотка в часах': '',
        'ставка в час': '',
        'премия': ''

    }

    for key in salary.keys():
        salary[key] = int(input(f'Ваша {key}: '))
    val = list(salary.values())
    res = val[0] * val[1] + val[2]
    print(f'Ваша зарплата: {res}')


if __name__ == '__main__':
    calc_salary()



