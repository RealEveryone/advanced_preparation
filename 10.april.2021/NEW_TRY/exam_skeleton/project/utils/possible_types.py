from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

possible_decorations = {'Ornament': Ornament,
                        'Plant': Plant}

possible_fish = {'FreshwaterFish': FreshwaterFish,
                 'SaltwaterFish': SaltwaterFish}

possible_aquariums = {'FreshwaterAquarium': FreshwaterAquarium,
                      'SaltwaterAquarium': SaltwaterAquarium}
