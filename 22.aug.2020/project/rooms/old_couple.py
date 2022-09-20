from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, name, pension_one, pension_two):
        super().__init__(name, self.calculate_budget(pension_one, pension_two), 2)
        self.room_cost = 15
        self.appliances = self.create_list_of_appliances()
        self.expenses = self.calculate_expenses(self.appliances)

    def create_list_of_appliances(self):
        result = []
        for _ in range(self.members_count):
            result.extend([TV(), Fridge(), Stove()])
        return result

    @staticmethod
    def calculate_budget(pension_one, pension_two):
        return pension_one + pension_two
