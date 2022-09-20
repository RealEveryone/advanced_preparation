class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

    def __len__(self):
        return len(self.drivers)

    def driver_in_race(self, given_driver):
        for driver in self.drivers:
            if driver.name == given_driver.name:
                return True
        return False

    def add(self, driver):
        self.drivers.append(driver)

    def fastest_cars(self):
        output = []
        fastest_drivers = list(sorted(self.drivers, key=lambda x: -x.car.speed_limit))
        for driver in fastest_drivers[:3]:
            driver.increase_wins()
            output.append(f"Driver {driver.name} wins the {self.name} race with a speed of {driver.car.speed_limit}.")
        return '\n'.join(output)



