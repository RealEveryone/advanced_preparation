from abc import ABC, abstractmethod


class Drink(ABC):
    def __init__(self, name, portion, price, brand):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Brand cannot be empty string or white space!")
        self.__brand = value

        # Price - may have props,  If code does not work check it out !

    @abstractmethod
    def __repr__(self):
        pass
