"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 100
    max_cargo = 500

    def __init__(self, max_cargo, weight, started, fuel, fuel_consumption):
        super(Plane, self).__init__(weight, started, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if self.cargo + cargo < self.max_cargo:
            self.cargo += cargo
        else:
            raise CargoOverload("Overload")

    def remove_all_cargo(self):
        __cargo = self.cargo
        self.cargo = 0
        return __cargo
