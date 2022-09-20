from project.possible_types import food_types, drink_types, table_types


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drink_menu = []
        self.table_repository = []
        self.total_income = 0

    def add_food(self, food_type, name, price):
        if name in [food.name for food in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type not in food_types:
            return
        self.food_menu.append(food_types[food_type](name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if name in [drink.name for drink in self.drink_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type not in drink_types:
            return
        self.drink_menu.append(drink_types[drink_type](name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_number in [table.table_number for table in self.table_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type not in table_types.keys():
            return
        self.table_repository.append(table_types[table_type](table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in reversed(self.table_repository):
            if table.capacity >= number_of_people and not table.is_reserved:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"
        # possibly it could be reversed search for table

    def search_table_by_number(self, table_number):
        for table in self.table_repository:
            if table.table_number == table_number:
                return table
        return None

    @staticmethod
    def return_if_exists(name, ll):
        for obj in ll:
            if obj.name == name:
                return obj
        return None

    def repository_search(self, ll, repository):
        existing = []
        non_existing = []
        for current in ll:
            result = self.return_if_exists(current, repository)
            if result:
                existing.append(result)
            else:
                non_existing.append(current)
        return existing, non_existing

    def order_food(self, table_number, *args):
        table = self.search_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"
        in_menu, not_in_menu = self.repository_search(args, self.food_menu)
        result = [f"Table {table_number} ordered:"]
        for food in in_menu:
            result.append(repr(food))
        result.append(f'{self.name} does not have in the menu:')
        for food in not_in_menu:
            result.append(food)
        return '\n'.join(result)

    def order_drink(self, table_number, *args):
        table = self.search_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"
        in_menu, not_in_menu = self.repository_search(args, self.drink_menu)
        result = [f"Table {table_number} ordered:"]
        for drink in in_menu:
            result.append(repr(drink))
        result.append(f'{self.name} does not have in the menu:')
        for drink in not_in_menu:
            result.append(drink)
        return '\n'.join(result)

    def leave_table(self, table_number):
        table = self.search_table_by_number(table_number)
        output = f'Table: {table_number}\nBill: {table.get_bill():.2f}'
        self.total_income += table.get_bill()
        table.clear()
        return output

    def get_free_tables_info(self):
        result = []
        for table in self.table_repository:
            if not table.is_reserved:
                info = table.free_table_info()
                result.append(info)
        return '\n'.join(result)

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'
