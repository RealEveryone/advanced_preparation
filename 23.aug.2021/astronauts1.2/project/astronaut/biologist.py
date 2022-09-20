from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    def __init__(self, name):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= 5

    def increase_oxygen(self, amount):
        self.oxygen += amount
