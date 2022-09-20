class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

    def extend_list(self, new_items):
        self.items.extend(new_items)

    def collectable_items(self):
        return self.items.copy()

