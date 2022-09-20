import os

from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.expenses + room.room_cost
        return f"Monthly consumption: {total}$."

    def pay(self):
        output = []
        for room in self.rooms:
            total_expenses = room.expenses + room.room_cost
            if total_expenses <= room.budget:
                room.budget -= total_expenses
                output.append(f"{room.family_name} paid {total_expenses}$ and have {room.budget}$ left.")
            else:
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return os.linesep.join(output).strip()

    def status(self):
        output = f"Total population: {sum([x.members_count for x in self.rooms])}\n"
        for room in self.rooms:
            output += f"{room.family_name} with {room.members_count} members. Budget: {room.budget}$," \
                      f" Expenses: {room.expenses}$\n"
            if len(room.children) > 0:
                for idx, child in enumerate(room.children):
                    output += f'--- Child {idx+1} monthly cost: {child.get_monthly_expense()}$\n'
            if len(room.appliances) > 0:
                output += f'{sum([ap.cost for ap in room.appliances])}$\n'
        return output.strip()

