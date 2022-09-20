class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet):
        self.planets.append(planet)

    def remove(self, planet):
        for idx, current in self.planets:
            if current == planet:
                self.planets.pop(idx)

    def find_by_name(self, name):
        for planet in self.planets:
            if planet.name == name:
                return planet
        return None
