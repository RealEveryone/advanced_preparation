class Player:
    CREATED_PLAYERS = []

    def __init__(self, name, age, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    def sustain_self(self, value):
        if self.stamina + value > 100:
            self.stamina = 100
        else:
            self.stamina += value

    def decrease_stamina(self, value):
        if self.stamina - value < 0:
            self.stamina = 0
        else:
            self.stamina -= value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Name not valid!")
        if value in Player.CREATED_PLAYERS:
            raise Exception(f"Name {value} is already used!")
        self.__name = value
        Player.CREATED_PLAYERS.append(value)

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or 100 < value:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"


