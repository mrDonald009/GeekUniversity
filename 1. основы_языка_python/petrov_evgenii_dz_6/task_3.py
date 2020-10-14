class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def total_income(self):
        total_income = (sum(self._income.values()))
        print(f'доход с учетом премии состовляет {total_income}')

    def get_full_name(self):
        print(f'полное имя сотрудника {self.surname} {self.name}')

user_1 = Position('Михаил', 'Сидоров', 'техник', 1000, 100)
user_2 = Position('Иван', 'Иванов', 'физик', 1000, 200)

print(user_1.name)
print(user_2.name)
user_1.get_full_name()
user_1.total_income()
user_2.get_full_name()
user_2.total_income()