from abc import ABC, abstractmethod


class Astronaut(ABC):
    OXY_UNITS = 10

    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @abstractmethod
    def breathe(self):
        pass

    def increase_oxygen(self, amount):
        self.oxygen += amount

    def add_to_backpack(self, value):
        self.backpack.append(value)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def details(self):
        backpack_items = 'none' if len(self.backpack) == 0 else ', '.join(self.backpack)
        result = [f"Name: {self.name}", f"Oxygen: {self.oxygen}", f"Backpack items: {backpack_items}"]
        return '\n'.join(result)