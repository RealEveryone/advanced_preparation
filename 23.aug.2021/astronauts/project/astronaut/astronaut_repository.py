class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        for idx, current in enumerate(self.astronauts):
            if current == astronaut:
                self.astronauts.pop(idx)

    def find_by_name(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return None

    def increase_astronaut_oxygen(self):
        for astronaut in self.astronauts:
            astronaut.increase_oxygen(10)

    def capable_astronauts(self):
        sorted_astronauts_by_oxygen = sorted(self.astronauts, key=lambda x: x.oxygen)
        capable_astronauts = []
        while len(capable_astronauts) < 5 and sorted_astronauts_by_oxygen:
            current_astronaut = sorted_astronauts_by_oxygen.pop()
            if current_astronaut.oxygen > 30:
                capable_astronauts.append(current_astronaut)
        return capable_astronauts

    def __iter__(self):
        for astronaut in self.astronauts:
            yield astronaut

