from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    ROOM_COST = 20

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, (salary_one + salary_two), 2)
        self.appliances = self.create_list_of_appliances([TV(), Fridge(), Laptop()], 2)
