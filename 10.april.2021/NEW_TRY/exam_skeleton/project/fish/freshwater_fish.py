from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    INCREASE_VALUE = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)

    @property
    def type(self):
        return 'FreshwaterFish'
