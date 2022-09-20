from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXY_UNITS = 15

    def __init__(self, name, oxygen=90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.OXY_UNITS
