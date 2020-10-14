class Road:
    def __init__(self, length=1, width=1):
        self._length = length
        self._width = width

    def result(self, kilogram, thickness=1):
        self._kilogram = kilogram
        self._thickness = thickness
        sum = ((self._length * self._width) * (self._kilogram * self._thickness) / 1000)
        print(f'масса асфальта {sum} т')

area = Road(20, 5000)
area.result(25, 5)
