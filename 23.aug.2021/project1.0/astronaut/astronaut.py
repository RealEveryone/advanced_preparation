from abc import ABC, abstractmethod


class Astronaut(ABC):
    UNITS_PER_BREATHE = 10

    @abstractmethod
    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen

    def breathe(self):
        self.oxygen -= self.UNITS_PER_BREATHE

    def increase_oxygen(self, amount):
        self.oxygen += amount


