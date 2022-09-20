from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decoration_list = []
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
        return sum([decoration.comfort for decoration in self.decoration_list])

    def add_fish(self, fish: object):
        if len(self.fish_list) == self.capacity:
            return "Not enough capacity."
        fish_type = fish.__class__.__name__
        fish_type = fish_type[:len(fish.__class__.__name__)-4]
        if fish_type not in self.__class__.__name__:
            return "Water not suitable."
        self.fish_list.append(fish)
        return f"Successfully added {fish.type()} to {self.name}."

    def remove_fish(self, fish: object):
        if fish in self.fish_list:
            self.fish_list.remove(fish)

    def add_decoration(self, decoration: object):
        self.decoration_list.append(decoration)

    @abstractmethod
    def feed(self):
        pass

    def __str__(self):
        output = [f'{self.name}:']
        if self.fish_list:
            fish_names = ", ".join([fish.name for fish in self.fish_list])
            output.append(f'Fish: {fish_names}')
        else:
            output.append(f'Fish: none')
        output.append(f'Decorations: {len(self.decoration_list)}')
        output.append(f'Comfort: {self.calculate_comfort()}')
        return '\n'.join(output)

    def __len__(self):
        return len(self.fish_list)

    def calculate_fish_value(self):
        return sum([fish.price for fish in self.fish_list])

    def calculate_decoration_value(self):
        return sum([decoration.price for decoration in self.decoration_list])
