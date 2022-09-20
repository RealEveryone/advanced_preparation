import os


class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    def add(self, driver):
        self.drivers.append(driver)

    def __len__(self):
        return len(self.drivers)

    def return_faster_racers(self):
        fastest_racers = []
        for driver in sorted(self.drivers, key=lambda x: -x.car.speed_limit):
            if len(fastest_racers) < 3:
                driver.win_race()
                fastest_racers.append(f"Driver {driver.name} wins the {self.name} race with a speed of "
                                      f"{driver.car.speed_limit}.")
        return os.linesep.join(fastest_racers)


    @staticmethod
    def __validate_name(name):
        if len(name) == 0:
            raise ValueError("Name cannot be an empty string!")