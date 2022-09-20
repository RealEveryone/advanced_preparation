from abc import ABC, abstractmethod


class BaseFish(ABC):
    INCREASE_VALUE = 5
    def __init__(self, name, species, size, price):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_string(value, 'name')
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__validate_string(value, 'species')
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_int(value)
        self.__price = value

    @staticmethod
    def __validate_int(value):
        if not isinstance(value, int) or value <= 0 :
            raise ValueError("Price cannot be equal to or below zero.")

    @staticmethod
    def __validate_string(value, ink):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError(f"Fish {ink} cannot be an empty string.")

    def eat(self):
        self.size += self.INCREASE_VALUE

    @property
    @abstractmethod
    def type(self):
        pass
