# Задание 4.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color.title()} {self.name} went.')

    def stop(self):
        print(f'{self.color.title()} {self.name} stopped.')

    def turn(self, direction):
        print(f'{self.color.title()} {self.name} turned to the {direction}.')

    def show_speed(self):
        print(f'{self.color.title()} {self.name} is moving at a speed of {self.speed}.')


class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        print(f'{self.color.title()} {self.name} is moving at a speed of {self.speed}.')
        if self.speed > 60:
            print('The car goes over the speed limit!')


class SportCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        print(f'{self.color.title()} {self.name} is moving at a speed of {self.speed}.')
        if self.speed > 40:
            print('The car goes over the speed limit!')


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


town_1 = TownCar(60, 'green', 'Opel', False)
town_2 = TownCar(70, 'green', 'Opel', False)
sport = SportCar(350, 'black', 'Lamborghini', False)
work_1 = WorkCar(50, 'white', 'Opel', False)
work_2 = WorkCar(40, 'black', 'Ford Police Interceptor', True)
police = PoliceCar(60, 'black', 'Ford Police Interceptor', True)

print(town_1.go(), town_1.stop(), town_1.turn('left'), town_1.is_police)
print(town_1.show_speed())
print(town_2.show_speed())
print(sport.name, sport.speed, sport.color, sport.is_police)
print(work_1.show_speed())
print(work_2.show_speed())
print(police.name, police.speed, police.color, police.is_police)
