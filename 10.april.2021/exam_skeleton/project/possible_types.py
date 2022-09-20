from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

possible_aquarium_types = {'FreshwaterAquarium': FreshwaterAquarium, 'SaltwaterAquarium': SaltwaterAquarium}
possible_fish_types = {'FreshwaterFish': FreshwaterFish, 'SaltwaterFish': SaltwaterFish}
possible_decoration_types = {'Ornament': Ornament, 'Plant': Plant}
