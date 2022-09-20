class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def astronaut_oxygen_maintenance(self):
        for astro in self.astronauts:
            astro.increase_oxygen(10)

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        for astro in self.astronauts:
            if astro.name == name:
                return astro
        return None

    def find_capable_astronauts_for_mission(self):
        capable_astronauts = []
        for astro in sorted(self.astronauts, key=lambda x: -x.oxygen):
            if astro.oxygen > 30 and len(capable_astronauts) < 5:
                capable_astronauts.append(astro)

        return capable_astronauts
