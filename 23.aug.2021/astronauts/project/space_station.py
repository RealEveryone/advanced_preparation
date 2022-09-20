from project.astronaut.astronaut_repository import AstronautRepository
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.possible_astronauts import astronauts_dict


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.unsuccessful_missions = 0

    def add_astronaut(self, astronaut_type, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            return f"{name} is already added."
        if astronaut_type not in astronauts_dict.keys():
            raise Exception("Astronaut type is not valid!")
        self.astronaut_repository.add(astronauts_dict[astronaut_type](name))

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        item_list = items.split(', ')
        planet = Planet(name)
        planet.extend_list(item_list)
        self.planet_repository.add(planet)

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)

    def recharge_oxygen(self):
        self.astronaut_repository.increase_astronaut_oxygen()

    def mission_progress(self, planet, suitable_astronauts):
        space_walks = 0
        collectable_items = planet.collectable_items()
        while suitable_astronauts:
            current_astronaut = suitable_astronauts.pop(0)
            space_walks += 1
            while current_astronaut.oxygen > 0:
                current_astronaut.breathe()
                if len(collectable_items) == 0:
                    self.successful_missions += 1
                    return f"Planet: {planet.name} was explored. " \
                           f"{space_walks} astronauts participated in collecting items."
                current_astronaut.add_to_backpack(collectable_items.pop())
        self.unsuccessful_missions += 1
        return "Mission is not completed."

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")
        suitable_astronauts = self.astronaut_repository.capable_astronauts()
        if len(suitable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        result_from_mission = self.mission_progress(planet, suitable_astronauts)
        return result_from_mission

    def report(self):
        output = [f'{self.successful_missions} successful missions!',
                  f'{self.unsuccessful_missions} missions were not completed!',
                  "Astronaut's info:"]
        for astronaut in self.astronaut_repository:
            output.append(astronaut.details())
        return '\n'.join(output)
