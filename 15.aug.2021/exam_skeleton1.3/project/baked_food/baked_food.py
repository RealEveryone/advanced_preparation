from abc import ABC, abstractmethod
from project.utils.validators import validate_string, validate_integer


class BakedFood(ABC):
    def __init__(self, name, portion, price):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_string(value, 'Name')
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        validate_integer(value, 'Price')
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"

    @property
    @abstractmethod
    def type(self):
        pass
