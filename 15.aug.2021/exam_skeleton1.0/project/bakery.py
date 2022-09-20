from project.mapped_product_types import food_dict, drink_dict, table_dict


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @staticmethod
    def exists_by_name(name, menu):
        for product in menu:
            if product.name == name:
                return product
        return False

    def find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    def find_free_table(self, number_of_people):
        for table in reversed(self.tables_repository):
            if not table.is_reserved and table.capacity >= number_of_people:
                return table
        return None

    def add_food(self, food_type, name, price):
        if food_type not in food_dict.keys():
            return
        if self.exists_by_name(name, self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")
        self.food_menu.append(food_dict[food_type](name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if drink_type not in drink_dict:
            return
        if self.exists_by_name(name, self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")
        self.drinks_menu.append(drink_dict[drink_type](name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_type not in table_dict:
            return
        if table_number in [table.table_number for table in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")
        self.tables_repository.append(table_dict[table_type](table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        table = self.find_free_table(number_of_people)
        if table is None:
            return "No available table for {number_of_people} people"
        table.reserve(number_of_people)
        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number, *food_names):
        table = self.find_table(table_number)
        if table is None:
            return f"Could not find table {table_number}"
        not_in_menu = ''
        in_menu = ''
        for name in food_names:
            food = self.exists_by_name(name, self.food_menu)
            if food:
                table.order_food(food)
                in_menu += repr(food) + '\n'
            else:
                not_in_menu += name + '\n'
        output = f'Table {table_number} ordered:\n'
        output += in_menu
        output += f'{self.name} does not have in the menu:\n'
        output += not_in_menu

        return output.strip()

    def order_drink(self, table_number, *drink_names):
        table = self.find_table(table_number)
        if table is None:
            return f"Could not find table {table_number}"
        not_in_menu = ''
        in_menu = ''
        for name in drink_names:
            drink = self.exists_by_name(name, self.drinks_menu)
            if drink:
                table.order_drink(drink)
                in_menu += repr(drink) + '\n'
            else:
                not_in_menu += name + '\n'
        output = f'Table {table_number} ordered:\n'
        output += in_menu
        output += f'{self.name} does not have in the menu:\n'
        output += not_in_menu

        return output.strip()

    def leave_table(self, table_number):
        table = self.find_table(table_number)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f'Table: {table_number}\nBill: {bill:.2f}'

    def get_free_tables_info(self):
        output = []
        for table in self.tables_repository:
            if not table.is_taken:
                output.append(repr(table))
        return '\n'.join(output)

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'
