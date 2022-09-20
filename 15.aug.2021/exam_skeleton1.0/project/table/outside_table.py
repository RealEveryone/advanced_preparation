from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if 51 < value <= 100:
            self.__table_number = value
        else:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")

    def free_table_info(self):
        return f"Table: {self.table_number}\nType: {self.__class__.__name__}\nCapacity: {self.capacity}"