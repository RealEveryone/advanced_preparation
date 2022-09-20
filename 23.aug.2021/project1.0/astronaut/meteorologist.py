from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    UNITS_PER_BREATHE = 15

    def __init__(self, name, oxygen=90):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []
