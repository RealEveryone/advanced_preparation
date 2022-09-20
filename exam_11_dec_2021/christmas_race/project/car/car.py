import sys
from abc import ABC, abstractmethod


class Car(ABC):
    DEFAULT_MIN_SPEED_LIMIT = -sys.maxsize
    DEFAULT_MAX_SPEED_LIMIT = sys.maxsize

    def __init__(self, model, speed_limit):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__validate_model(value)
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        self.__validate_speed_limit(value)
        self.__speed_limit = value

    @property
    @abstractmethod
    def type(self):
        pass

    def change_status(self):
        self.is_taken = not self.is_taken

    @staticmethod
    def __validate_model(model):
        if len(model) < 4:
            raise ValueError(f"Model {model} is less than 4 symbols!")

    def __validate_speed_limit(self, speed):
        if self.DEFAULT_MIN_SPEED_LIMIT > speed or self.DEFAULT_MAX_SPEED_LIMIT < speed:
            raise ValueError(f"Invalid speed limit!"
                             f" Must be between {self.DEFAULT_MIN_SPEED_LIMIT} and {self.DEFAULT_MAX_SPEED_LIMIT}!")
