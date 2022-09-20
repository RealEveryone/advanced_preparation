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
        if len(value.strip()) == 0:
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    def increase_wins(self):
        self.number_of_wins += 1

    def set_car(self, car):
        self.car = car


