from abc import ABC, abstractmethod


class Astronaut(ABC):

    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @abstractmethod
    def breathe(self):
        pass  # class attr may be a problem

    @abstractmethod
    def increase_oxygen(self, amount):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def details(self):
        backpack = 'none'
        if len(backpack) > 0:
            backpack = ', '.join(self.backpack)
        output = f'Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {backpack}'
        return output

    def add_to_backpack(self, item):
        self.backpack.append(item)
