class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        self.direction = None

    def go(self):
        if self.speed > 0:
            print(f'машина {self.name}, {self.color} цвета, едет со скоростью {self.speed}')
        else:
            print(f'машина {self.name}, {self.color} цвета, стоит')

    def stop(self):
        if self.speed == 0:
            print(f'машина {self.name}, {self.color} цвета, стоит')
        else:
            print(f'машина {self.name}, {self.color} цвета, едет со скоростью {self.speed}')

    def turn(self, direction):
        print(f'машина {self.name}, {self.color} цвета, повернула {direction}')

    def show_speed(self):
        print(f'скорость автомобиля {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'автомобиль {self.name} превышает скоростной режим')
        else:
            print(f'автомобиль {self.name}, едет со скоростью {self.speed}')

class SportCar(Car):
    def go(self):
        if self.speed > 0:
            print(f'машина {self.name}, {self.color} цвета, едет со скоростью {self.speed}')
        else:
            print(f'машина {self.name}, {self.color} цвета, стоит')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'автомобиль {self.name} превыщает скоростной режим')
        else:
            print(f'автомобиль {self.name}, едет со скоростью {self.speed}')

class PoliceCar(Car):
    def go(self):
        if self.speed > 0:
            print(f'машина {self.name}, {self.color} цвета, едет со скоростью {self.speed}')
        else:
            print(f'машина {self.name}, {self.color} цвета, стоит')

user_1 = Car(0, 'красного', 'ferrary')
user_2 = TownCar(180, 'черного', 'toyota')
user_3 = SportCar(300, 'белого', 'ford')
user_4 = WorkCar(60, 'синего', 'bigtrack')
user_1.stop()
user_2.go()
user_3.turn('налево')
user_4.show_speed()