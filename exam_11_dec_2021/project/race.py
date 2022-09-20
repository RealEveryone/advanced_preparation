class Race:
    def __init__(self, name):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            ValueError("Name cannot be an empty string!")
        self.__name = value

    def __len__(self):
        return len(self.drivers)

    def fastest_drivers(self):
        sorted_list = list(sorted(self.drivers, key=lambda x: -x.car.speed_limit))
        for driver in sorted_list[:3]:
            driver.number_of_wins += 1
        return sorted_list

