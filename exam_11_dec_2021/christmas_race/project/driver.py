class Driver:
    def __init__(self, name):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    def win_race(self):
        self.number_of_wins += 1

    def set_car(self, car):
        self.car = car

    @staticmethod
    def __validate_name(name):
        if len(name.strip()) == 0:
            raise ValueError("Name should contain at least one character!")
