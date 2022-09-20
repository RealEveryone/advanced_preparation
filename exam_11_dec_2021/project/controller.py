import sys


from change_name.muscle_car import MuscleCar
from change_name.sports_car import SportsCar
from driver import Driver
from race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    @staticmethod
    def __instance_exists(name, names_in_instance):
        if name in names_in_instance:
            return True
        return False

    def __find_driver(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver
        return None

    def __find_car(self, car_type):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        return None

    def __find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        return None

    def create_car(self, car_type, model, speed_limit):
        if self.__instance_exists(model, [x.model for x in self.cars]):
            raise Exception(f'Car {model} is already created!')
        if car_type not in ['SportsCar', 'MuscleCar']:
            return
        new_car = getattr(sys.modules[__name__], car_type)(model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        if self.__instance_exists(driver_name, [x.name for x in self.drivers]):
            raise Exception(f'Driver {driver_name} is already created!')
        self.drivers.append(Driver(driver_name))
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name):
        if self.__instance_exists(race_name, [x.name for x in self.races]):
            raise Exception(f'Race {race_name} is already created!')
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver = self.__find_driver(driver_name)
        if driver is None:
            raise Exception(f'Driver {driver_name} could not be found!')
        car = self.__find_car(car_type)
        if car is None:
            raise Exception(f'Car {car_type} could not be found!')

        if driver.car is not None:
            output = f'Driver {driver_name} changed his car from {driver.car.model} to {car.model}.'
            driver.car.is_taken = False
            car.is_taken = True

            driver.car = car
            return output

        driver.car = car
        car.is_taken = True
        return f'Driver {driver_name} chose the car {car.model}.'

    def add_driver_to_race(self, race_name, driver_name):
        race = self.__find_race(race_name)
        if race is None:
            raise Exception(f'Race {race_name} could not be found!')
        driver = self.__find_driver(driver_name)
        if driver is None:
            raise Exception(f'Driver {driver_name} could not be found!')

        if driver.car is None:
            raise Exception(f'Driver {driver_name} could not participate in the race!')

        if driver in race.drivers:
            return f'Driver {driver_name} is already added in {race_name} race.'

        race.drivers.append(driver)
        return f'Driver {driver_name} added in {race_name} race.'

    def start_race(self, race_name):
        race = self.__find_race(race_name)
        if race is None:
            raise Exception(f'Race {race_name} could not be found!')
        if len(race) < 3:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')
        output = ''
        for current in race.fastest_drivers()[:3]:
            driver = current.name
            speed_limit = str(current.car.speed_limit)
            output += f'Driver {driver} wins the {race_name} race with a speed of {speed_limit}.\n'
        return output.strip()