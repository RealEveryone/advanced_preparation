from abc import ABC, abstractmethod


class Car(ABC):
    MIN_SPEED_LIMIT = 0
    MAX_SPEED_LIMIT = 0

    @abstractmethod
    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f'Model {value} is less than 4 symbols!')
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if self.MIN_SPEED_LIMIT > value or value > self.MAX_SPEED_LIMIT:
            raise ValueError(f'Invalid speed limit! '
                             f'Must be between {self.MIN_SPEED_LIMIT} and {self.MAX_SPEED_LIMIT}!')
        self.__speed_limit = value
