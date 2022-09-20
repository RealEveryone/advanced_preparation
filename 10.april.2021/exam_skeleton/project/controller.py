from project.decoration.decoration_repository import DecorationRepository
from project.possible_types import possible_fish_types, possible_aquarium_types, possible_decoration_types


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in possible_aquarium_types.keys():
            return "Invalid aquarium type."
        self.aquariums.append(possible_aquarium_types[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in possible_decoration_types.keys():
            return "Invalid decoration type."
        self.decorations_repository.add(possible_decoration_types[decoration_type]())
        return f"Successfully added {decoration_type}."

    def find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        aquarium = self.find_aquarium_by_name(aquarium_name)
        aquarium.add_decoration(decoration)
        self.decorations_repository.remove(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in possible_fish_types.keys():
            return f"There isn't a fish of type {fish_type}."
        aquarium = self.find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return
        return aquarium.add_fish(possible_fish_types[fish_type](fish_name, fish_species, price))

    def feed_fish(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f'Fish fed: {len(aquarium)}'

    def calculate_value(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        fish_value = aquarium.calculate_fish_value()
        decoration_value = aquarium.calculate_decoration_value()
        value = fish_value + decoration_value
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = []
        for aquarium in self.aquariums:
            result.append(str(aquarium))
        return '\n'.join(result)
