
class AstronautRepository:

    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return None

    def __getitem__(self, item):
        return self.astronauts[item]

    def natural_astronauts_selection_by_oxygen(self):
        astronauts_selection = list(sorted(self.astronauts, key=lambda x: -x.oxygen))
        capable_astronauts = []

        while len(capable_astronauts) < 5 and astronauts_selection:
            astronaut = astronauts_selection.pop()
            if astronaut.oxygen > 30:
                capable_astronauts.append(astronaut)
        return capable_astronauts




