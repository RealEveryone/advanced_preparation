from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    UNITS_PER_BREATHE = 5

    def __init__(self, name, oxygen=70):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []
