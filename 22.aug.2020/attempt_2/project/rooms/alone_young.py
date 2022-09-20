from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    def __init__(self, family_name, salary):
        self.appliances = self.create_list_of_appliances([TV()], 1)
        super().__init__(family_name, salary, 1)
