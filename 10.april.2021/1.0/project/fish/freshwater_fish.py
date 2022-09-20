from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):

    def __init__(self, name, species, price, size=3):
        super().__init__(name, species, size, price)

    def eat(self):
        self.size += 3

