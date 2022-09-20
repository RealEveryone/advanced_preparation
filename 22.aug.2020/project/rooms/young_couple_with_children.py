from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, name, salary_one, salary_two, *children):
        super().__init__(name, self.calculate_budget(salary_one, salary_two), 2+len(children))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = self.create_list_of_appliances()
        self.expenses = self.calculate_expenses(self.appliances, self.children)  # Possible Error

    @staticmethod
    def calculate_budget(salary_one, salary_two):
        return salary_one + salary_two

    def create_list_of_appliances(self):
        result = []
        for _ in range(2 + len(self.children)):
            result.extend([TV(), Fridge(), Laptop()])
        return result

