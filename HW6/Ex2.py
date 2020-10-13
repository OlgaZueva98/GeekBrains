# Задание 2.

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass_per_m = 0.025
        self._thickness = 5

    def mass_count(self):
        mass = self._length * self._width * self._mass_per_m * self._thickness
        print(f'Для покрытия всего дорожного полотна потребуется {mass} т. асфальта.')


asph_mass = Road(20, 5000)
asph_mass.mass_count()
