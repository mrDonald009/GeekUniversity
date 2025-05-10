from time import sleep
class TrafficLight:
    def __init__(self):
        self._color = ['red', 'yellow', 'green']

    def running(self, delay_second):
        second = [7, 2, delay_second]
        i = 0
        while i < len(self._color):
            for color in self._color:
                print(color)
                sleep(second[i])
                i += 1

user = TrafficLight()
user.running(7)
