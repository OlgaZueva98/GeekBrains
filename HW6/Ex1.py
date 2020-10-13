# Задание 1.

from time import sleep


class TrafficLight:

    def __init__(self, colors):
        self.__color = colors

    def running(self):
        i = 0
        while i < 3:
            print(self.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)

            i += 1


traffic_light = TrafficLight(['red', 'yellow', 'green'])
traffic_light.running()
