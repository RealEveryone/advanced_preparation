from project.driver import Driver
from project.race import Race
from project.utils.possible_car_types import possible_car_types_dict


class Controller:
    CAR_TYPES = ["MuscleCar", "SportsCar"]

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        self.__check_if_car_model_exists(model)
        if car_type not in self.CAR_TYPES:
            return
        self.cars.append(possible_car_types_dict[car_type](model, speed_limit))
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        if self.__find_obj_by_name(driver_name, self.drivers) is not None:
            raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        if self.__find_obj_by_name(race_name, self.races) is not None:
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver = self.__find_obj_by_name(driver_name, self.drivers)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if car_type not in self.CAR_TYPES:
            return
        car = self.__return_car_by_type_if_exists(car_type)
        if car is None:
            raise Exception(f"Car {car_type} could not be found!")
        car.change_status()
        if driver.car is not None:
            previous_driver_car = driver.car
            previous_driver_car.change_status()
            driver.set_car(car)
            return f"Driver {driver_name} changed his car from {previous_driver_car.model} to {car.model}."
        driver.set_car(car)
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race = self.__find_obj_by_name(race_name, self.races)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self.__find_obj_by_name(driver_name, self.drivers)
        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.add(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self.__find_obj_by_name(race_name, self.races)
        if race is None:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        return race.return_faster_racers()

    def __check_if_car_model_exists(self, model):
        if model in [car.model for car in self.cars]:
            raise Exception(f"Car {model} is already created!")

    def __return_car_by_type_if_exists(self, car_type):
        for car in reversed(self.cars):
            if car.type == car_type and not car.is_taken:
                return car
        return None

    @staticmethod
    def __find_obj_by_name(name, repository):
        for obj in repository:
            if obj.name == name:
                return obj
        return None

