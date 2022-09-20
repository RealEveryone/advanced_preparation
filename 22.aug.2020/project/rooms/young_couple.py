from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, name, salary_one, salary_two):
        super().__init__(name, self.calculate_budget(salary_one, salary_two), 2)
        self.room_cost = 20
        self.appliances = self.create_list_of_appliances()
        self.expenses = self.calculate_expenses(self.appliances)

    def create_list_of_appliances(self):
        result = []
        for _ in range(self.members_count):
            result.extend([TV(), Fridge(), Laptop()])
        return result

    @staticmethod
    def calculate_budget(salary_one, salary_two):
        return salary_one + salary_two

