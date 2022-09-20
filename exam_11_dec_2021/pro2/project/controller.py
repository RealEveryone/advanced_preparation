from project.driver import Driver
from project.possible_types import car_types_dict
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        if model in [car.model for car in self.cars]:
            raise Exception(f"Car {model} is already created!")
        if car_type not in car_types_dict.keys():
            return
        car = car_types_dict[car_type](model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."

    @staticmethod
    def return_if_exists(given_name, ll):
        for obj in ll:
            if obj.name == given_name:
                return obj
        return None

    def create_driver(self, driver_name):
        if driver_name in [driver.name for driver in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        if race_name in [race.name for race in self.races]:
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def get_last_possible_car_type(self, car_type):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        return None

    def add_car_to_driver(self, driver_name, car_type):
        driver = self.return_if_exists(driver_name, self.drivers)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        car = self.get_last_possible_car_type(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")
        car.set_to_taken()
        if driver.car is not None:
            driver_old_car = driver.car
            driver_old_car.set_to_free()
            driver.set_car(car)
            return f"Driver {driver_name} changed his car from {driver_old_car.model} to {car.model}."
        driver.set_car(car)
        return F"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race = self.return_if_exists(race_name, self.races)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self.return_if_exists(driver_name, self.drivers)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if race.driver_in_race(driver):
            return f"Driver {driver_name} is already added in {race_name} race."
        race.add(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self.return_if_exists(race_name, self.races)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race) < 3:
            raise Exception(F"Race {race_name} cannot start with less than 3 participants!")
        result = race.fastest_cars()
        return result
