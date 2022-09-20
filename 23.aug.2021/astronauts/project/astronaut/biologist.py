from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXY_UNITS = 5

    def __init__(self, name, oxygen=70):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.OXY_UNITS
