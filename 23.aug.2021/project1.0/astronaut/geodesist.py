from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):

    def __init__(self, name, oxygen=50):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []
