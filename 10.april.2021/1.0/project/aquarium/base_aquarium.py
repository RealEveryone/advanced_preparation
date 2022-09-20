from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

        self.decorations = []
        self.fish_list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        total_comfort = 0
        for decoration in self.decorations:
            total_comfort += decoration.comfort
        return total_comfort

    def feed(self):
        for fish in self.fish_list:
            fish.eat()

    def not_enough_capacity(self):
        return self.capacity < len(self.fish_list)

    def add_fish(self, fish):
        if fish.fish_type not in ['FreshwaterFish', 'SaltwaterFish']:
            return f"There isn't a fish of type {fish.fish_type}."
        if self.not_enough_capacity():
            return f"Not enough capacity."
        if fish.fish_type not in str(self.__class__.__name__):
            return f"Water not suitable."
        self.fish_list.append(fish)
        return f"Successfully added {fish.fish_type} to {self.name}."

    def calculate_value_of_aquarium(self):
        result = 0
        for decoration in self.decorations:
            result += decoration.price
        for fish in self.fish_list:
            result += fish.price
        return result

    def __str__(self):
        output = f'{self.name}:\n'

        if self.fish_list:
            output += ', '.join([f.name for f in self.fish_list])
        else:
            output += 'None'

        output += '\n'
        output += f'Decorations: {len(self.decorations)}\n'
        output += f'Comfort: {self.calculate_comfort()}'

        return output