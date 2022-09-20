class Room:
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.appliances = []
        self.expenses = 0
        self.room_cost = 0

    def calculate_expenses(self, *args):
        result = 0
        for list_of_objects in args:
            for current in list_of_objects:
                result += current.get_monthly_expense()
        self.expenses = result
        return result

    def total_expenses(self):
        return self.expenses + self.room_cost

    def total_members_count(self):
        return self.members_count + len(self.children)

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self.__expenses = value

