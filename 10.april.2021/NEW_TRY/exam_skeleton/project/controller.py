from project.decoration.decoration_repository import DecorationRepository
from project.utils.possible_types import possible_aquariums, possible_fish, possible_decorations


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in possible_aquariums.keys():
            return "Invalid aquarium type."
        self.aquariums.append(possible_aquariums[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in possible_decorations.keys():
            return "Invalid decoration type."
        self.decorations_repository.add(possible_decorations[decoration_type]())
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.__return_object_if_exists(aquarium_name, self.aquariums)
        if aquarium is None:
            return
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == 'None':
            return f"There isn't a decoration of type {decoration_type}."
        aquarium.add_decoration(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in possible_fish:
            return f"There isn't a fish of type {fish_type}."
        aquarium = self.__return_object_if_exists(aquarium_name, self.aquariums)
        if aquarium is None:
            return
        return aquarium.add_fish(possible_fish[fish_type](fish_name, fish_species, price))

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__return_object_if_exists(aquarium_name, self.aquariums)
        aquarium.feed()
        return f"Fish fed: {len(aquarium)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__return_object_if_exists(aquarium_name, self.aquariums)
        return f"The value of Aquarium {aquarium_name} is {aquarium.calc():.2f}."

    def report(self):
        output = ''
        for aquarium in self.aquariums:
            output += str(aquarium) + '\n'
        return output.strip()

    @staticmethod
    def __return_object_if_exists(name, repository):
        for obj in repository:
            if obj.name == name:
                return obj
        return None

