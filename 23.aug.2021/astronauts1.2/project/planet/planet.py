class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

    def append_to_items(self, value_list):
        self.items.extend(value_list)
