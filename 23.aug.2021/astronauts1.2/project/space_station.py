from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.possible_astronauts_types import astronauts_type


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_complete_missions = 0

    def create_astronaut_of_type(self, given_type, name):
        if given_type not in astronauts_type:
            raise Exception("Astronaut type is not valid!")
        self.astronaut_repository.add(astronauts_type[given_type](name))
        return f"Successfully added {given_type}: {name}."

    @staticmethod
    def created_planet(name, items_string):
        items = items_string.split(', ')
        created_planet = Planet(name)
        created_planet.append_to_items(items)
        return created_planet

    def add_astronaut(self, astronaut_type, name):
        if self.astronaut_repository.find_by_name(name) is not None:
            return f"{name} is already added."
        return self.create_astronaut_of_type(astronaut_type, name)

    def add_planet(self, name, items_string: str):
        if self.planet_repository.find_by_name(name) is not None:
            return f"{name} is already added."
        self.planet_repository.add(self.created_planet(name, items_string))
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        self.astronaut_repository.astronaut_oxygen_maintenance()

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        capable_astronauts = self.astronaut_repository.find_capable_astronauts_for_mission()
        if len(capable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        space_walks = 0
        while capable_astronauts:
            # if len(planet.items) == 0:
            #     self.successful_missions += 1
            #     return f"Planet: {planet_name} was explored." \
            #            f" {space_walks} astronauts participated in collecting items."
            astro = capable_astronauts.pop(0)
            space_walks += 1
            while astro.oxygen > 0:
                if len(planet.items) == 0:
                    self.successful_missions += 1
                    return f"Planet: {planet_name} was explored." \
                           f" {space_walks} astronauts participated in collecting items."
                astro.add_to_backpack(planet.items.pop())
                astro.breathe()
        self.not_complete_missions += 1
        return "Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!\n" \
                 f"{self.not_complete_missions} missions were not completed!\n" \
                 f"Astronauts' info:\n"
        for astro in self.astronaut_repository.astronauts:
            details = astro.details()
            result += details + '\n'
        return result.strip()


# space_station = SpaceStation()
# space_station.add_planet('Planet1', 'Item1, Item2, Item3, Item4, Item5')
# space_station.add_astronaut('Biologist', 'Name1')
# space_station.add_astronaut('Biologist', 'Name2')
# space_station.add_astronaut('Geodesist', 'Name3')
# space_station.add_astronaut('Meteorologist', 'Name4')
# print(space_station.recharge_oxygen())
# print(space_station.send_on_mission('Planet1'))
# print(space_station.report())
# print(space_station.retire_astronaut('Name1'))
