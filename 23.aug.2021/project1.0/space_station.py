import sys
from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type, name):
        if self.astronaut_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        if astronaut_type not in ['Biologist', 'Geodesist', 'Meteorologist']:
            raise Exception("Astronaut type is not valid!")

        new_astronaut = getattr(sys.modules[__name__], astronaut_type)(name)
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name) is not None:
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items.extend(items)
        self.planet_repository.add(new_planet)

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        capable_astronauts = self.astronaut_repository.natural_astronauts_selection_by_oxygen()
        if len(capable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        space_walks = 0
        while planet.items:
            astronaut = capable_astronauts.pop(0)
            space_walks += 1
            for _ in range(len(planet.items)):
                current_item = planet.items.pop()
                astronaut.backpack.append(current_item)
                astronaut.breathe()
                if astronaut.oxygen <= 0 or len(planet.items) == 0:
                    break
            if len(capable_astronauts) == 0:
                self.unsuccessful_missions += 1
                return "Mission is not completed."
        self.successful_missions += 1
        return f"Planet: {planet_name} was explored. {space_walks} astronauts participated in collecting items."

    def report(self):
        output = f"{self.successful_missions} successful missions!\n" \
                 f"{self.unsuccessful_missions} missions were not completed!"
        output += f"Astronauts' info:\n"
        for astronaut in self.astronaut_repository:
            astronaut_backpack = ", ".join(astronaut.backpack)
            output += f'Name: {astronaut.name}\nOxygen: {astronaut.oxygen}\n' \
                      f'Backpack items: {"none" if astronaut_backpack == "" else astronaut_backpack}\n'

        return output.strip()

