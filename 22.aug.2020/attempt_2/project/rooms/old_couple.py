from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    ROOM_COST = 15

    def __init__(self, family_name, pension_one, pension_two):
        self.appliances = self.create_list_of_appliances([TV(), Fridge(), Stove()], 2)
        super().__init__(family_name, (pension_one + pension_two), 2)
