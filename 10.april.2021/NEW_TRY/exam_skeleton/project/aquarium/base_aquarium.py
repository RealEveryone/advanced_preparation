from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    FISH_TYPES = ["FreshwaterFish", "SaltwaterFish"]

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    def calculate_comfort(self):
        return sum([decor.comfort for decor in self.decorations])

    def add_fish(self, fish):
        if len(self) == self.capacity:
            return "Not enough capacity."
        if fish.type not in self.FISH_TYPES:
            return
        if fish.type[:len(fish.type) - 4] not in self.type:
            return "Water not suitable."
        self.fish.append(fish)
        return f"Successfully added {fish.type} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fishes = 'none'
        if self.fish:
            fishes = ' '.join([x.name for x in self.fish])
        return f"{self.name}:\n" \
               f"Fish: {fishes}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"

    @staticmethod
    def __validate_name(name):
        if len(name) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")

    def __len__(self):
        return len(self.fish)

    def calc(self):
        return sum([x.price for x in self.fish]) \
               + sum([x.price for x in self.decorations])

    @property
    @abstractmethod
    def type(self):
        pass
