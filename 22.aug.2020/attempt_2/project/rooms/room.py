class Room:
    ROOM_COST = 10

    def __init__(self, family_name, budget, members_count, children=list, appliances=list):
        self.family_name = family_name
        self.budget = budget
        self.children = children

        self.members_count = members_count + len(self.children)
        self.room_cost = self.ROOM_COST
        self.appliances = appliances
        self.expenses = self.calculate_expenses(self.appliances, self.children)

    @staticmethod
    def calculate_expenses(*args):
        total = 0
        for list_of_elements in args:
            for current in list_of_elements:
                total += current.get_monthly_expense()
        return total

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        self.__validate_expenses(value)
        self.__expenses = value

    @staticmethod
    def __validate_expenses(value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

    @staticmethod
    def create_list_of_appliances(list_of_appliances, people_count):
        ll = []
        for _ in range(people_count):
            ll.extend(list_of_appliances)
        return ll
