from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    ROOM_COST = 30

    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, (salary_one + salary_two), 2)
        self.children.extend(children)

        self.appliances = self.create_list_of_appliances([TV(), Fridge(), Laptop()], self.members_count)

