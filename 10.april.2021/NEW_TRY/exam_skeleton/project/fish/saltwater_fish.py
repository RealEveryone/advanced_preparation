from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    INCREASE_VALUE = 2

    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)

    @property
    def type(self):
        return 'SaltwaterFish'
