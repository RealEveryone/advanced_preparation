from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name):
        super().__init__(name, 50)

    def feed(self):
        for fish in self.fish_list:
            fish.eat()
