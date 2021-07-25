from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=100, started=False, fuel=40, fuel_consumption=2):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError('Low Fuel')

    def move(self, distance):
        if self.fuel_consumption*distance < self.fuel:
            self.fuel -= self.fuel_consumption*distance
        else:
            raise NotEnoughFuel('Low on fuel')

