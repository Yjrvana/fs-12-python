import random


class Transport:
    def __init__(self, speed, km):
        self.__speed = speed
        self.__current_km = 0

    @property
    def speed(self):
        return self.__speed

    @property
    def current_km(self):
        return self.__current_km

    def step(self):
        self.__current_km += self.__speed


class Tram(Transport):
    def __init__(self, speed, km, passengers):
        super().__init__(speed, km)
        self.__passengers = passengers

    def make_stop(self, end=False):
        self.__passengers -= random.randint(0, self.__passengers)
        self.__passengers += random.randint(0, 10)
        if end:
            self.__passengers = 0


class Car(Transport):
    def __init__(self, speed, km, max_fuel, current_fuel):
        super().__init__(speed, km)
        self.__max_fuel = max_fuel
        self.__current_fuel = current_fuel

    def step(self):
        if self.__current_fuel == 0:
            return
        super().step()

    def fill_up(self):
        self.__current_fuel = self.__max_fuel
