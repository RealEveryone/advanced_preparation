import sys
from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class Controller:
    def __init__(self):
        self.decoration_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type not in ['FreshwaterAquarium', 'SaltwaterAquarium']:
            return "Invalid aquarium type."
        self.aquariums.append(getattr(sys.modules[__name__], aquarium_type)(aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type not in ['Ornament', 'Plant']:
            return 'Invalid decoration type.'
        self.decoration_repository.add(getattr(sys.modules[__name__], decoration_type)())
        return f"Successfully added {decoration_type}."

    def find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
        return None

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decoration_repository.find_by_type(decoration_type)
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        aquarium = self.find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return

        aquarium.decoration.append(decoration)
        self.decoration_repository.remove(decoration)
        return f'Successfully added {decoration_type} to {aquarium_name}.'

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        fish = getattr(sys.modules[__name__], fish_type)(fish_name, fish_species, price)
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f'Fish fed: {len(aquarium.fish_list)}'

    def calculate_value(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        return f'The value of Aquarium {aquarium_name} is {aquarium.calculate_value_of_aquarium:.2f}.'

    def report(self):
        output = []
        for aquarium in self.aquariums:
            output.append(str(aquarium))
        return '\n'.join(output)




